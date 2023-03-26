import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import json


def compute():
    members_df = pd.read_csv('data/Справочник участников оборота товаров.csv')

    points_df = pd.read_csv('data/Справочник торговых точек.csv')

    points_df.loc[points_df['region_code'] == 51, 'city_with_type'] = "Мурманская"
    points_df.loc[points_df['region_code'] == 77, 'city_with_type'] = "Москва"
    points_df.loc[points_df['region_code'] == 50, 'city_with_type'] = "Мо"
    points_df.loc[points_df['region_code'] == 78, 'city_with_type'] = "Спб"
    points_df['postal_code'] = points_df['postal_code'].fillna(0).astype(int)

    products_df = pd.read_csv('data/Справочник продукции.csv')

    products_df['country'] = products_df['country'].fillna('0')
    products_df['volume'] = products_df['volume'].fillna(1)
    products_df.loc[products_df['volume'] == "НЕ КЛАССИФИЦИРОВАНО", 'volume'] = 1

    inn_points_region_code_equal = points_df.set_index('inn').join(members_df.set_index('inn')['region_code'],
                                                                   rsuffix='_inn').query(
        "region_code == region_code_inn").index.unique()

    inn_points_region_code_NOT_equal = set(members_df['inn'].unique()) - set(inn_points_region_code_equal)
    inn_points_region_code_NOT_equal = np.array(list(inn_points_region_code_NOT_equal))
    inn_points_region_code_NOT_equal.size


    movement_df = pd.read_csv('data/Агрегированные данные о перемещениях товаров между участниками с 2021-11-22 по 2022-11-21.csv')
    out_df = pd.read_csv('data/Агрегированные данные о выводе товаров из оборота с 2021-11-22 по 2022-11-21.csv')
    in_df = pd.read_csv('data/Агрегированные данные о вводе товаров в оборот с 2021-11-22 по 2022-11-21.csv')

    factory_in = pd.read_csv(
        'data/Дополнительные датасеты для продукта для производителя/Данные о вводе товаров в оборот с 2021-11-22 по 2022-11-21 один производитель.csv')
    factory_out = pd.read_csv(
        'data/Дополнительные датасеты для продукта для производителя/Данные о выводе товаров из оборота с 2021-11-22 по 2022-11-21 один производитель.csv')
    factory_move = pd.read_csv(
        'data/Дополнительные датасеты для продукта для производителя/Данные о перемещениях товаров между участниками с 2021-11-22 по 2022-11-21 один производитель.csv')

    factory_out = factory_out.query('type_operation == "Продажа конечному потребителю в точке продаж"')

    factory_out_joined = pd.read_csv('data_joined/factory_out_joined.csv')
    factory_move_joined = pd.read_csv('data_joined/factory_move_joined.csv')

    factory_out_joined['date'] = pd.to_datetime(factory_out_joined['date'])
    factory_move_joined['date'] = pd.to_datetime(factory_move_joined['date'])

    factory_out_joined['quarter'] = factory_out_joined['date'].dt.quarter
    factory_move_joined['quarter'] = factory_move_joined['date'].dt.quarter

    PRODUCT_SHORT = "9199AB529CF62D4BDB7E8B1D7459001D"
    REGION_CODE = 77
    # POSTAL_CODE = 0
    # TIME_H = 0 #
    GROUP_PERIOD = 'week'  # 'dayy' 'month' 'quarter'

    one_prod_region = factory_move_joined.query(f"product_short_name == '{PRODUCT_SHORT}'").query(
        f"region_code_rec_inn == {REGION_CODE}")

    # Фильтрация ИНН на критерий нахождения в points_df
    receiver_inns = factory_move_joined.query(f"product_short_name == '{PRODUCT_SHORT}'").query(
        f"region_code_rec_inn == {REGION_CODE}")['receiver_inn'].unique()
    list_points_inn = set(receiver_inns).intersection(points_df['inn'].unique())

    # factory_move_joined.query("product_short_name == '9199AB529CF62D4BDB7E8B1D7459001D'").query(f"region_code_rec_inn == {REGION_CODE}").groupby(['receiver_inn']).count()['sender_inn'].sort_values(ascending=False)

    one_prod_region_filtered = one_prod_region[one_prod_region['receiver_inn'].isin(list_points_inn)]
    one_prod_region_filtered = one_prod_region_filtered.query("receiver_inn != 'DA62EC79660CF21AC37A260DA6F642C4'")

    one_prod_region_filtered_moving = one_prod_region_filtered.groupby([GROUP_PERIOD])['cnt_moved'].sum()  # Группировка
    one_prod_region_filtered_moving.head(2)

    one_good_type_region = factory_out_joined.query(f"product_short_name == '{PRODUCT_SHORT}'").query(
        f"region_code == {REGION_CODE}")

    one_good_type_region_sum = one_good_type_region.groupby(['week'])['cnt'].sum()  # Группировка
    one_good_type_region_sum.head(2)

    # factory_move_joined.set_index('receiver_inn').join(points_df.drop_duplicates().set_index('inn')['postal_code'], how='inner')\ # consider left
    # .reset_index().rename(columns={'index':'receiver_inn'}).drop(columns=['Unnamed: 0'])\
    # .drop_duplicates(subset=list(factory_move_joined.columns)[1:])

    # cumsum
    df_total = pd.DataFrame({'move': one_prod_region_filtered_moving, 'out': one_good_type_region_sum})
    df_total['move_out'] = df_total['move'] - df_total['out']

    df_total['move_cumsum'] = df_total['move'].cumsum()
    df_total['out_cumsum'] = df_total['out'].cumsum()
    df_total['cum_sum_diff'] = df_total['move_cumsum'] - df_total['out_cumsum']

    df_total = df_total[['move', 'out', 'cum_sum_diff']]

    df_total.rename(columns={'move': 'прибытие', 'out': 'выбытие', 'cum_sum_diff': 'остаток'}).to_csv(
        'df_tolal_prod_reg.csv')

    # pd.date_range('2021-11-22', '2022-11-21', freq='D').week

    # import datetime
    # d = f"{2022}-W{6}"
    # r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
    # print(str(r).split(' ')[0])

    week_to_dt_pd = factory_move_joined.sort_values(by='dt').groupby(['week']).first().sort_values(by='dt')[
        'dt'].reset_index()

    week_nums = np.unique(pd.date_range('2021-11-22', '2022-11-21', freq='D').week.values)

    # for i, row in df_total.iterrows():
    #     print(row['cum_sum_diff'])

    # obj_json = {}

    # date_idx = 1
    # obj_arr = []
    # for i in range(0, 30):
    #     obj_one = {}
    #     obj_one['date'] = f"2022-01-{date_idx}"
    #     obj_one['stock'] = 450
    #     obj_one['green_estimate'] = 300 + random.randint(50, 100)
    #     obj_one['yellow_estimate'] = 100 + random.randint(20, 50)
    #     obj_one['red_estimate'] = 50 + random.randint(20, 35)
    #     obj_arr.append(obj_one)
    #     date_idx +=1

    # obj_json['message'] = obj_arr

    # with open("./example.json", "w") as json_file:
    #     json.dump(obj_json, json_file)


if __name__ == "__main__":
    compute()
    
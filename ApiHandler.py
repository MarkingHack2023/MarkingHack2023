from flask_restful import Api, Resource, reqparse

class Function(Resource):
    def get(self):
        return {
            'status': 'SUCCESS',
            'message': [
{"date": "2022-01-1", "stock": 380, "green_estimate": 387, "yellow_estimate": 126, "red_estimate": 72},
 {"date": "2022-01-2", "stock": 350, "green_estimate": 369, "yellow_estimate": 120, "red_estimate": 74},
 {"date": "2022-01-3", "stock": 390, "green_estimate": 389, "yellow_estimate": 124, "red_estimate": 81},
 {"date": "2022-01-4", "stock": 10, "green_estimate": 363, "yellow_estimate": 127, "red_estimate": 74},
 {"date": "2022-01-5", "stock": 400, "green_estimate": 396, "yellow_estimate": 121, "red_estimate": 80},
 {"date": "2022-01-6", "stock": 350, "green_estimate": 355, "yellow_estimate": 132, "red_estimate": 74},
 {"date": "2022-01-7", "stock": 390, "green_estimate": 395, "yellow_estimate": 130, "red_estimate": 82},
 {"date": "2022-01-8", "stock": 380, "green_estimate": 395, "yellow_estimate": 147, "red_estimate": 72},
 {"date": "2022-01-9", "stock": 120, "green_estimate": 357, "yellow_estimate": 132, "red_estimate": 70},
 {"date": "2022-01-10", "stock": 70, "green_estimate": 395, "yellow_estimate": 130, "red_estimate": 72},
 {"date": "2022-01-11", "stock": 80, "green_estimate": 360, "yellow_estimate": 128, "red_estimate": 77},
 {"date": "2022-01-12", "stock": 300, "green_estimate": 362, "yellow_estimate": 150, "red_estimate": 76},
 {"date": "2022-01-13", "stock": 290, "green_estimate": 384, "yellow_estimate": 145, "red_estimate": 84},
 {"date": "2022-01-14", "stock": 280, "green_estimate": 360, "yellow_estimate": 121, "red_estimate": 78},
 {"date": "2022-01-15", "stock": 260, "green_estimate": 395, "yellow_estimate": 143, "red_estimate": 78},
 {"date": "2022-01-16", "stock": 230, "green_estimate": 356, "yellow_estimate": 125, "red_estimate": 74},
 {"date": "2022-01-17", "stock": 100, "green_estimate": 387, "yellow_estimate": 135, "red_estimate": 78},
 {"date": "2022-01-18", "stock": 80, "green_estimate": 384, "yellow_estimate": 127, "red_estimate": 79},
 {"date": "2022-01-19", "stock": 60, "green_estimate": 357, "yellow_estimate": 132, "red_estimate": 84},
 {"date": "2022-01-20", "stock": 433, "green_estimate": 377, "yellow_estimate": 134, "red_estimate": 73},
 {"date": "2022-01-21", "stock": 450, "green_estimate": 399, "yellow_estimate": 148, "red_estimate": 71},
 {"date": "2022-01-22", "stock": 420, "green_estimate": 390, "yellow_estimate": 146, "red_estimate": 75},
 {"date": "2022-01-23", "stock": 410, "green_estimate": 385, "yellow_estimate": 139, "red_estimate": 83},
 {"date": "2022-01-24", "stock": 350, "green_estimate": 373, "yellow_estimate": 134, "red_estimate": 82},
 {"date": "2022-01-25", "stock": 120, "green_estimate": 394, "yellow_estimate": 134, "red_estimate": 72},
 {"date": "2022-01-26", "stock": 250, "green_estimate": 381, "yellow_estimate": 137, "red_estimate": 71},
 {"date": "2022-01-27", "stock": 170, "green_estimate": 382, "yellow_estimate": 143, "red_estimate": 73},
 {"date": "2022-01-28", "stock": 315, "green_estimate": 367, "yellow_estimate": 122, "red_estimate": 82},
 {"date": "2022-01-29", "stock": 300, "green_estimate": 365, "yellow_estimate": 145, "red_estimate": 70},
 {"date": "2022-01-30", "stock": 350, "green_estimate": 357, "yellow_estimate": 148, "red_estimate": 78}
                       ]
        }
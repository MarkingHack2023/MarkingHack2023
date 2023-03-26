import csv
from flask import Flask, jsonify, render_template, send_from_directory, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from ApiHandler import Function

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.debug = True

api = Api(app)

@app.route('/', defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/data', methods=['POST'])
def get_filtered_data():
    filters = request.get_json()

    products = [
        {'name': 'Product A', 'short_name': 'A', 'price': 1099},
        {'name': 'Product B', 'short_name': 'B', 'price': 1999},
        {'name': 'Product C', 'short_name': 'C', 'price': 599}
    ]
    regions = [
        {'name': 'Moscow', 'code': 77},
        {'name': 'MO', 'code': 50}
    ]
    postcodes = [
        {'code': 141031, 'region_code': 50},
        {'code': 109012, 'region_code': 77}
    ]
    filtered_data = []
    for product in products:
        if product['short_name'] == filters['product_short_name']:
            for region in regions:
                if region['code'] == filters['region_code']:
                    for postcode in postcodes:
                        if postcode['code'] == filters['postal_code'] and postcode['region_code'] == region['code']:
                            filtered_data.append({
                                'product_name': product['name'],
                                'region_name': region['name'],
                                'postcode': postcode['code'],
                                'price': product['price']
                            })

    return jsonify({'data': filtered_data})

api.add_resource(Function, '/api/function')
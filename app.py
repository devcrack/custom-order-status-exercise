# stdlib

# 3rd-party
from flask import Flask, request, jsonify

# local
from api.customer_orders import get_orders_from_file


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/get-order-status/csv/', methods=['GET'])
def get_orders_status_from_csv():
#     if request.method == "GET":
    return 'No method allowed'


@app.route('/custom-order-status/')
def exercise():
    return jsonify(get_orders_from_file())




if __name__ == '__main__':
    app.run()

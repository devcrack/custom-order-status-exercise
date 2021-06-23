from flask import Flask, request

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
    return 'Hello World!'




if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request, make_response
from VendingMachine import VendingMachine
app = Flask(__name__)

goodyear = VendingMachine("1")

@app.route('/', methods=['PUT'])
def put_change():
    data = request.get_json()
    try: 
        result = goodyear.deposit(data.get("coin"))
        response = make_response('', 204)
        response.headers['X-Coins'] = result
        return response
    except Exception as err:
        return make_response(jsonify({"Error": str(err)}), 500)

@app.route('/', methods=['DELETE'])
def delete_coins():
    result = goodyear.return_coins()
    response = make_response('', 204)
    response.headers['X-Coins'] = result
    return response

@app.route('/inventory', methods=['GET'])
def get_inventory():
    result = goodyear.get_inventory()
    response = make_response(jsonify(result), 200)
    return response

@app.route('/inventory/<id>', methods=['GET'])
def get_item_inventory(id):
    result = goodyear.get_inventory(id)
    response = make_response(jsonify(result), 200)
    return response

if __name__ == "__main__":
    app.run(debug=True)
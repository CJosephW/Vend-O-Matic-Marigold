from flask import Flask, jsonify, request, make_response
from VendingMachine import VendingMachine
app = Flask(__name__)

CokeSpyware = VendingMachine("1")

@app.route('/', methods=['PUT'])
def putChange():
    data = request.get_json()
    try: 
        result = CokeSpyware.deposit(data.get("coin"))
        if isinstance(result, int):
            response = make_response('', 204)
            response.headers['X-Coins'] = result
            return response
    except Exception as err:
        return make_response(jsonify({"Error": str(err)}), 500)
    
    
if __name__ == "__main__":
    app.run(debug=True)
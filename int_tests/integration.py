# simple 'integration' test script
import requests

url = 'http://localhost:5000/'

put_response = requests.put(url, json={'coin':1})

if put_response.status_code == 204 and put_response.headers.get("X-Coins") == '1':
    print('PUT / (deposit coin) OKAY')

delete_response = requests.delete(url)

if delete_response.status_code == 204 and delete_response.headers.get("X-Coins") == '1':
    print('DELETE / (return coins) OKAY')

get_inventory_response = requests.get(url + 'inventory')

if get_inventory_response.status_code == 200 and get_inventory_response.json() == { "A1": 5, "A2": 5, "A3":5}:
    print('GET /inventory OKAY')

get_item_inventory_response = requests.get(url + 'inventory/A1')

if get_item_inventory_response.status_code == 200 and get_item_inventory_response.json() == 5:
    print('GET /inventory/<id> OKAY')
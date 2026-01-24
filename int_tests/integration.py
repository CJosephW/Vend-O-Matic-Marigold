# simple 'integration' test script
import requests

url = 'http://localhost:5000/'

put_response = requests.put(url, json={'coin':1})

if put_response.status_code == 204 and put_response.headers.get("X-Coins") == '1':
    print('PUT / (deposit coin) OKAY')

delete_response = requests.delete(url)

if delete_response.status_code == 204 and delete_response.headers.get("X-Coins") == '1':
    print('DELETE / (return coins) OKAY')



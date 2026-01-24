# simple 'integration' test script
import requests

url = 'http://localhost:5000/'
response = requests.put(url, json={'coin':1})

if response.status_code == 204:
    print('PUT / (deposit coin) OKAY')


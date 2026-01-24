import json
from errors import CoinInsertionError

file = open('database.json')
data = json.load(file)

class VendingMachine:
    def __init__(self, id):
        machine_data = data["machines"][f"{id}"]
        self.inventory = machine_data["inventory"]
        self.coins = machine_data["coins"]

    def deposit(self, coinInput):
        if coinInput != 1:  
            raise CoinInsertionError("This machine only accepts single US Quarters")
        
        self.coins += coinInput
        return self.coins
    
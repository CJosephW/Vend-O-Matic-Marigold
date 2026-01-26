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
    
    def return_coins(self):
        coins_to_return = self.coins
        self.coins = 0
        return coins_to_return
    
    def get_inventory(self, id=None):
        if(id is not None):
            return self.inventory[f"{id}"]["amount"]
        inventory_count =  {
            item: self.inventory[f"{item}"]["amount"]
            for item in self.inventory
        }
        return inventory_count
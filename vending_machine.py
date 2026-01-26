import json
from errors import CoinInsertionError, ItemOutOfStockError, InsufficentCoinError

file = open("database.json")
data = json.load(file)

class VendingMachine:
    def __init__(self, id):
        machine_data = data["machines"][f"{id}"]
        self.inventory = machine_data["inventory"]
        self.coins = machine_data["coins"]
        self.items_vended = 0

    def deposit(self, coinInput):
        if coinInput != 1:  
            raise CoinInsertionError("This machine only accepts single US Quarters")
        self.coins += coinInput
        return self.coins
    
    def end_transaction(self):
        coins_to_return = self.coins
        self.coins = 0
        # only dispense single beverage per transaction
        self.items_vended = 0
        return coins_to_return
    
    def get_inventory(self, id=None):
        if(id is not None):
            return self.inventory[f"{id}"]["amount"]
        # if no ID is passed return the entire inventory"s remaining quantity
        inventory_count =  {
            item: self.inventory[f"{item}"]["amount"]
            for item in self.inventory
        }
        return inventory_count
    
    def vend_item(self, id):
        price = self.inventory[f"{id}"]["price"]
        if (self.get_inventory(id) == 0):
            raise ItemOutOfStockError(f"{id} is currently out of stock")
        if (self.coins < price):
            raise InsufficentCoinError(self.coins)
        
        self.coins -= price 
        self.inventory[f"{id}"]["amount"] -= 1
        self.items_vended += 1
        return {
            "remaining": self.inventory[f"{id}"]["amount"], 
            "items_vended": self.items_vended,
            "coins": self.end_transaction()
            }
    
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from vending_machine import VendingMachine
from errors import CoinInsertionError, InsufficentCoinError, ItemOutOfStockError

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine("1")
        self.vm_two = VendingMachine("2")

    def test_returns_coin_count(self):
        self.assertEqual(self.vm.deposit(1), 1)
    
    def test_returns_exception(self):
        with self.assertRaises(CoinInsertionError):
            self.vm.deposit(2)
            
    def test_returns_coins_inserted(self):
        self.vm.deposit(1)
        self.assertEqual(self.vm.end_transaction(), 1)

    def test_returs_correct_inventory(self):
        self.assertEqual(self.vm.get_inventory(), {"A1":5, "A2":5, "A3":5})
        
    def test_returns_correct_item_inventory(self):
        self.assertEqual(self.vm_two.get_inventory("A2"), 4)

    def test_vend_item(self):
        self.vm_two.deposit(1)
        self.vm_two.deposit(1)
        self.assertEqual(self.vm_two.vend_item("A1"), {
            "remaining": 4,
            "items_vended": 1,
            "coins": 0
        })
        
    def test_insufficent_coin_error(self):        
        with self.assertRaises(InsufficentCoinError):
            self.vm_two.vend_item("A1")
    def test_out_of_stock_error(self):
        with self.assertRaises(ItemOutOfStockError):
            self.vm_two.vend_item("A3")

if __name__ == '__main__':
    unittest.main()
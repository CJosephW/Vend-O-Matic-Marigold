import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from VendingMachine import VendingMachine
from errors import CoinInsertionError

class TestDeposit(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine("1")
    
    def test_returns_coin_count(self):
        """Test deposit of 1 coin"""
        self.assertEqual(self.vm.deposit(1), 1)
    
    def test_returns_exception(self):
        with self.assertRaises(CoinInsertionError):
            self.vm.deposit(2)
        
class TestDelete(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine("1")
    
    def test_returns_coins_inserted(self):
        self.vm.deposit(1)
        self.assertEqual(self.vm.returnCoins(), 1)

if __name__ == '__main__':
    unittest.main()
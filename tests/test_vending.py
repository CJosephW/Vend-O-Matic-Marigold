import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from VendingMachine import VendingMachine
from errors import CoinInsertionError

class TestPutRequests(unittest.TestCase):
    def test_returns_coin_count(self):
        coke = VendingMachine("1")
        self.assertEqual(coke.deposit(1), 1)
    def test_returns_exception(self):
        coke = VendingMachine("1")
        with self.assertRaises(CoinInsertionError):
            coke.deposit(2)
        
if __name__ == '__main__':
    unittest.main()
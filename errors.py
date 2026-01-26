
class CoinInsertionError(Exception):
    """Invalid Insertion"""
    pass
class ItemOutOfStockError(Exception):
    """Item Out of Stock"""
    pass
class InsufficentCoinError(Exception):
    "Insufficent Coins"
    pass
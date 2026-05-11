# exchange_connector.py
import ccxt
import asyncio
from config import BINANCE_API_KEY, BINANCE_API_SECRET, BINANCE_TESTNET

class ExchangeConnector:
    """Handles all exchange communication - no trading logic here"""
    
    def __init__(self):
        if BINANCE_TESTNET:
            self.exchange = ccxt.binance({
                'apiKey': BINANCE_API_KEY,
                'secret': BINANCE_API_SECRET,
                'options': {'defaultType': 'future'},
                'urls': {'api': 'https://testnet.binancefuture.com'}
            })
        else:
            self.exchange = ccxt.binance({
                'apiKey': BINANCE_API_KEY,
                'secret': BINANCE_API_SECRET
            })
    
    async def fetch_ohlcv(self, symbol, timeframe="1h", limit=100):
        """Fetch OHLCV data"""
        try:
            data = self.exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
    
    async def fetch_balance(self):
        """Fetch account balance"""
        try:
            balance = self.exchange.fetch_balance()
            return balance['total']
        except Exception as e:
            print(f"Error fetching balance: {e}")
            return None
    
    async def create_order(self, symbol, side, amount, order_type="market"):
        """Create an order (NO STRATEGY LOGIC - just execution)"""
        try:
            order = self.exchange.create_order(symbol, order_type, side, amount)
            return order
        except Exception as e:
            print(f"Error creating order: {e}")
            return None
    
    async def fetch_open_orders(self, symbol):
        """Fetch open orders"""
        try:
            orders = self.exchange.fetch_open_orders(symbol)
            return orders
        except Exception as e:
            print(f"Error fetching orders: {e}")
            return None
    
    async def cancel_all_orders(self, symbol):
        """Cancel all open orders (for kill-switch)"""
        try:
            self.exchange.cancel_all_orders(symbol)
            return True
        except Exception as e:
            print(f"Error canceling orders: {e}")
            return False

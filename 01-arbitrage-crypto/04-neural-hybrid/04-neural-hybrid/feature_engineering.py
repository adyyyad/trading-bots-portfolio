# feature_engineering.py
import pandas as pd
import numpy as np

class FeatureEngineer:
    """
    Feature engineering for the LSTM model
    Shows WHAT features I use, but not the proprietary combinations
    """
    
    def __init__(self):
        self.feature_names = [
            # Price-based features
            'returns_1h', 'returns_4h', 'returns_24h',
            'log_returns', 'realized_volatility',
            
            # Technical indicators
            'rsi_14', 'macd', 'macd_signal', 'macd_histogram',
            'bb_upper', 'bb_lower', 'bb_position', 'atr_14',
            
            # Order book features (if available)
            'bid_ask_imbalance', 'order_book_depth',
            
            # Volume features
            'volume_delta', 'vwap_deviation',
        ]
    
    def calculate_features(self, ohlcv_data):
        """
        Calculate features from OHLCV data
        
        Args:
            ohlcv_data: list of [timestamp, open, high, low, close, volume]
        
        Returns:
            DataFrame with calculated features
        """
        df = self._ohlcv_to_dataframe(ohlcv_data)
        
        features = pd.DataFrame(index=df.index)
        
        # Price returns (public knowledge - safe to show)
        features['returns_1h'] = df['close'].pct_change(1)
        features['returns_4h'] = df['close'].pct_change(4)
        features['returns_24h'] = df['close'].pct_change(24)
        
        # RSI (standard formula - safe)
        features['rsi_14'] = self._calculate_rsi(df['close'], 14)
        
        # ATR (standard formula - safe)
        features['atr_14'] = self._calculate_atr(df, 14)
        
        # Volume features
        features['volume_delta'] = df['volume'].diff()
        
        # Remove NaN values
        features = features.dropna()
        
        return features
    
    def _ohlcv_to_dataframe(self, data):
        """Convert CCXT format to pandas DataFrame"""
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df
    
    def _calculate_rsi(self, prices, period=14):
        """Standard RSI calculation - safe to show"""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    def _calculate_atr(self, df, period=14):
        """Standard ATR calculation - safe to show"""
        high_low = df['high'] - df['low']
        high_close = (df['high'] - df['close'].shift()).abs()
        low_close = (df['low'] - df['close'].shift()).abs()
        tr = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)
        atr = tr.rolling(window=period).mean()
        return atr

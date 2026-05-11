# Exchange configuration
BINANCE_API_KEY = "your_api_key_here"
BINANCE_API_SECRET = "your_api_secret_here"

BINANCE_TESTNET = True  # Use testnet for development

# Trading parameters
SYMBOL = "BTC/USDT"
TIMEFRAME = "1h"
LOOKBACK_BARS = 60

# Risk parameters
MAX_POSITION_SIZE = 0.1  # 10% of portfolio
MAX_DAILY_LOSS = 0.03    # 3% daily loss limit
MAX_DRAWDOWN = 0.10      # 10% max drawdown

# Model paths
LSTM_MODEL_PATH = "models/lstm_v3.h5"
RL_MODEL_PATH = "models/ppo_trading_model.zip"

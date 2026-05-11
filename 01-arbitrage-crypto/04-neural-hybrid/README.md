
# Neural Hybrid Trading System (LSTM + Reinforcement Learning)

## Overview

This is my flagship trading system – a hybrid architecture that combines **LSTM neural networks** for market prediction with **Reinforcement Learning** for optimal execution.

Unlike traditional bots that use fixed rules or simple indicators, this system **learns continuously** from market conditions and adapts its strategy in real-time.

### Key Capabilities

| Component | Technology | What It Does |
|-----------|------------|---------------|
| **Predictor** | LSTM (Long Short-Term Memory) | Forecasts price direction and volatility |
| **Executor** | PPO (Proximal Policy Optimization) | Decides position sizing, entry/exit timing |
| **Risk Manager** | Custom rules + RL constraints | Limits drawdown, manages position exposure |
| **Orchestrator** | Python asyncio | Coordinates all components, handles API calls |

### Supported Assets

- ✅ Crypto (Binance, Bybit, Coinbase)
- ✅ Forex (OANDA, Interactive Brokers)
- ✅ Stocks / ETFs (Alpaca)

## Architecture

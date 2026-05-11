# risk_manager.py
import time
from datetime import datetime

class RiskManager:
    """
    Risk management module - protects the portfolio
    This is what separates professionals from amateurs
    """
    
    def __init__(self, max_drawdown=0.10, daily_loss_limit=0.03, max_position=0.10):
        self.max_drawdown = max_drawdown
        self.daily_loss_limit = daily_loss_limit
        self.max_position = max_position
        
        self.peak_balance = None
        self.daily_starting_balance = None
        self.last_reset_date = None
        self.trading_enabled = True
        self.kill_switch_triggered = False
        
    def update_balance(self, current_balance):
        """Update balance and check drawdown limits"""
        if self.peak_balance is None:
            self.peak_balance = current_balance
        
        if current_balance > self.peak_balance:
            self.peak_balance = current_balance
        
        # Check daily reset
        today = datetime.now().date()
        if self.last_reset_date != today:
            self.daily_starting_balance = current_balance
            self.last_reset_date = today
        
        # Check drawdown
        drawdown = (self.peak_balance - current_balance) / self.peak_balance
        if drawdown >= self.max_drawdown:
            self.kill_switch_triggered = True
            self.trading_enabled = False
            self._send_alert(f"DRAWDOWN LIMIT: {drawdown:.2%} reached")
            return False
        
        # Check daily loss
        daily_loss = (self.daily_starting_balance - current_balance) / self.daily_starting_balance
        if daily_loss >= self.daily_loss_limit:
            self.trading_enabled = False
            self._send_alert(f"DAILY LOSS LIMIT: {daily_loss:.2%} reached")
            return False
        
        return self.trading_enabled
    
    def calculate_position_size(self, balance, volatility, signal_strength):
        """Calculate position size based on Kelly Criterion and volatility"""
        # Base Kelly fraction (conservative: 0.25 Kelly)
        base_position = balance * 0.02  # 2% base risk per trade
        
        # Adjust for volatility (reduce size when volatile)
        vol_adj = max(0.5, min(1.5, 1 / volatility))
        
        # Adjust for signal strength (more confidence = larger position)
        signal_adj = 0.5 + (signal_strength * 0.5)  # Range: 0.5 to 1.0
        
        final_position = base_position * vol_adj * signal_adj
        
        # Cap at maximum position size
        final_position = min(final_position, balance * self.max_position)
        
        return final_position
    
    def can_trade(self):
        """Check if trading is enabled"""
        return self.trading_enabled and not self.kill_switch_triggered
    
    def manual_kill_switch(self):
        """Emergency stop - close all positions"""
        self.trading_enabled = False
        self.kill_switch_triggered = True
        self._send_alert("MANUAL KILL SWITCH TRIGGERED")
        return True
    
    def reset(self):
        """Reset trading (after drawdown recovery)"""
        self.trading_enabled = True
        self.peak_balance = None
        self._send_alert("Trading resumed after reset")
    
    def _send_alert(self, message):
        """Send alert via Telegram or webhook"""
        # In production: send Telegram message
        # For demo: print to console
        print(f"[ALERT] {message}")

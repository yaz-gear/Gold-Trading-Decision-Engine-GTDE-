import numpy as np

def calculate_returns(prices):
    return prices.pct_change().fillna(0)

def sharpe_ratio(returns, risk_free_rate=0.0):
    excess = returns - risk_free_rate
    return np.mean(excess) / np.std(excess) if np.std(excess) != 0 else 0

def max_drawdown(equity_curve):
    peak = equity_curve.expanding(min_periods=1).max()
    drawdown = (equity_curve - peak) / peak
    return drawdown.min()

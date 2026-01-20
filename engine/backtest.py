from utils.metrics import sharpe_ratio, max_drawdown

def backtest(df):
    returns = df['equity'].pct_change().fillna(0)
    return {
        "final_equity": df['equity'].iloc[-1],
        "sharpe_ratio": sharpe_ratio(returns),
        "max_drawdown": max_drawdown(df['equity'])
    }

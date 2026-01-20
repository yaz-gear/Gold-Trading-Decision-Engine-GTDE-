def volatility(series, window=14):
    return series.pct_change().rolling(window).std()

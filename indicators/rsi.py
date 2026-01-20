import numpy as np

def rsi(series, window=14):
    delta = series.diff()
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)

    avg_gain = series.copy()
    avg_loss = series.copy()

    avg_gain.iloc[window:] = gain[window:]
    avg_loss.iloc[window:] = loss[window:]

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

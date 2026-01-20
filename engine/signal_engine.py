def generate_signal(row):
    score = 0

    if row['close'] > row['sma_fast']:
        score += 1
    if row['close'] < row['sma_slow']:
        score -= 1

    if row['rsi'] < 30:
        score += 1
    elif row['rsi'] > 70:
        score -= 1

    if row['macd_hist'] > 0:
        score += 1
    else:
        score -= 1

    if score >= 2:
        return "BUY"
    elif score <= -2:
        return "SELL"
    return "HOLD"

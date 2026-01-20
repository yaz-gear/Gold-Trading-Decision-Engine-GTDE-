def apply_strategy(df):
    position = 0
    entry_price = 0
    equity = 100000
    equity_curve = []

    for _, row in df.iterrows():
        if row['signal'] == "BUY" and position == 0:
            position = equity / row['close']
            entry_price = row['close']
            equity = 0

        elif row['signal'] == "SELL" and position > 0:
            equity = position * row['close']
            position = 0

        total_equity = equity + position * row['close']
        equity_curve.append(total_equity)

    df['equity'] = equity_curve
    return df

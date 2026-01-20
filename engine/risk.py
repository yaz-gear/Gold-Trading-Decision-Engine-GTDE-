def position_size(capital, risk_per_trade, stop_loss_pct):
    risk_amount = capital * risk_per_trade
    return risk_amount / stop_loss_pct

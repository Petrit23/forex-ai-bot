def calculate_position_size(balance, risk_per_trade, stop_loss_pips, pip_value):
    risk_amount = balance * risk_per_trade
    lot = risk_amount / (stop_loss_pips * pip_value)
    return round(lot, 2)

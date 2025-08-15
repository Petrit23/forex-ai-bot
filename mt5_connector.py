import MetaTrader5 as mt5
import pandas as pd
from config import MT5_LOGIN, MT5_PASSWORD, MT5_SERVER, SYMBOL

def mt5_initialize():
    if not mt5.initialize():
        raise RuntimeError('MT5 initialization failed')
    authorized = mt5.login(MT5_LOGIN, password=MT5_PASSWORD, server=MT5_SERVER)
    if not authorized:
        raise RuntimeError('MT5 login failed')

def fetch_data(timeframe=mt5.TIMEFRAME_M1, bars=1000):
    rates = mt5.copy_rates_from_pos(SYMBOL, timeframe, 0, bars)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def send_order(action, lot, price=None, sl=None, tp=None):
    symbol_info = mt5.symbol_info(SYMBOL)
    if not symbol_info.visible:
        mt5.symbol_select(SYMBOL, True)
    order_type = mt5.ORDER_TYPE_BUY if action == 'buy' else mt5.ORDER_TYPE_SELL
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": SYMBOL,
        "volume": lot,
        "type": order_type,
        "price": price or mt5.symbol_info_tick(SYMBOL).ask,
        "sl": sl,
        "tp": tp,
        "deviation": 20,
        "magic": 42,
        "comment": "AI Trade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }
    result = mt5.order_send(request)
    return result

def shutdown():
    mt5.shutdown()

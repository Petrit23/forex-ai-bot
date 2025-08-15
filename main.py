from mt5_connector import mt5_initialize, fetch_data, send_order, shutdown
from ai_strategy import ai_decision, train_on_historical
from config import LOT
from utils import setup_logger
from telegram_bot import run_telegram_bot
import threading
import time

logger = setup_logger()
def trading_loop():
    mt5_initialize()
    while True:
        df = fetch_data()
        action = ai_decision(df)
        if action == 1:
            logger.info("AI: BUY signal")
            send_order('buy', LOT)
        elif action == -1:
            logger.info("AI: SELL signal")
            send_order('sell', LOT)
        else:
            logger.info("AI: HOLD")
        time.sleep(60)
    shutdown()

if __name__ == "__main__":
    t = threading.Thread(target=trading_loop)
    t.start()
    run_telegram_bot()

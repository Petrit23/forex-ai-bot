import logging

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
    return logging.getLogger('forex-bot')

def format_trade_result(result):
    if result.retcode == 10009:
        return f"Trade executed: {result.order}"
    else:
        return f"Trade failed: {result.retcode}"

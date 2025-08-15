# Forex AI Trading Bot

This project is an automated trading bot for Forex using MetaTrader 5 and AI-based strategies. It connects to MetaTrader 5 for trading, uses a simple AI model to make decisions, and allows interaction via Telegram.

---

## Features

- Connects to MetaTrader 5 (MT5) for live trading or demo accounts
- Uses a simple AI (machine learning) model to decide when to buy, sell, or hold
- Telegram bot interface for trade commands and account monitoring
- Modular code: easy to add new strategies or risk management rules

---

## Setup

### 1. Prerequisites

- **Python 3.8+**
- **MetaTrader 5** terminal installed and logged in (demo recommended)
- **Telegram bot token** (create via [@BotFather](https://t.me/botfather))
- **Telegram chat/user ID** (get via [@userinfobot](https://t.me/userinfobot))

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure

Edit `config.py`:
- Fill in your MetaTrader 5 login, password, server
- Add your Telegram bot token and chat ID

### 4. Run the Bot

```bash
python main.py
```

---

## Usage

- Talk to your Telegram bot with `/start`, `/status`, `/balance`, `/trade`, `/close`
- The bot will monitor the market and use AI to suggest or execute trades

---

## AI Model

- Uses historical price data and moving average crossovers as features
- Can be retrained with new data to enhance performance

---

## File Structure

- `main.py` – Main entry point and event loop
- `config.py` – User and API configuration
- `mt5_connector.py` – MetaTrader 5 integration
- `ai_strategy.py` – AI/ML strategy logic and training
- `risk_manager.py` – Position sizing and risk controls
- `utils.py` – Logging and helpers
- `telegram_bot.py` – Telegram interface

---

## Disclaimer

**This code is for educational/demo use. Trading is risky; use a demo account!**

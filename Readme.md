# 🤖 Trade Remote CLI 

This project is a Trade Remote CLI, a professional-grade command-line tool designed to interface directly with the Binance Futures Testnet. It’s built to give traders (or developers) a fast, automated way to execute orders without using a web browser.

# 2. 🏗️ Project Architecture

## 3.Install Dependencies
```bash
pip install python-binance python-dotenv
```

## 4.Configure API Keys
Open client.py or your .env file and ensure your Binance Testnet API Key and Secret are correctly set.

## 5.📖 How to Run the Bot
The bot uses argparse for a professional CLI experience. You can view the help section at any time:

```bash
python cli.py --help
```
## Help Section Overview
```bash
--symbol: The trading pair (e.g., BTCUSDT, ETHUSDT).

--side: Direction of the trade (BUY or SELL).

--type: Type of order (MARKET, LIMIT, STOP_LIMIT).

--qty: Amount of the asset to trade.

--price: Target price (Required for LIMIT and STOP_LIMIT).

--stopprice: Trigger price (Required for STOP_LIMIT).

```

# 💻 Demo CLI Commands
## 1. Market Orders
Execute a trade immediately at the current market price.

```bash
# Buy 0.002 BTC at Market Price
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.002
2. Limit Orders
Place an order to buy or sell at a specific price.
```

```bash
# Sell 0.002 BTC when the price hits $100,000
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.002 --price 100000
3. Stop-Limit Orders (Risk Management)
The order is placed only after the trigger (Stop Price) is hit.
```
```bash
# Breakout Buy: Trigger at $100,000, buy up to $100,050
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --qty 0.002 --price 100050 --stopprice 100000
```
## 📝 Important Notes
Minimum Notional: Binance Futures requires trades to have a minimum value (usually >$50). If your trade fails, try increasing the --qty.


## Testnet Only: This bot is configured for the Testnet environment to ensure safe testing of strategies.

## Logs: Check bot.log for a full history of your trading activity.

## Status: Clear, runnable, and validated prefrences.

# License
[MIT]
(https://choosealicense.com/licenses/mit/)
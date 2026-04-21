import argparse
from validators import validate_symbol, validate_trade_option
from orders import buy_the_order, sell_the_order
from logging_config import setup_logging

def main():

    setup_logging()
    # 1. Initialize the Parser
    parser = argparse.ArgumentParser(description="Binance Futures Bot")

    # 2. Define the Arguments
    parser.add_argument("--symbol", type=str, required=True, help="Target Symbol")
    parser.add_argument("--type", type=str, required=True, choices=['MARKET', 'LIMIT','STOP_LIMIT'], help="Order Type")
    parser.add_argument("--side", type=str, required=True, choices=['BUY', 'SELL'], help="Trade Side")
    parser.add_argument("--qty", type=str, required=True, help="Quantity to trade")
    parser.add_argument("--price", type=str, help="Price (Required for LIMIT)")
    parser.add_argument("--stopprice", type=str, help="The price that triggers the Stop-Limit order")

    # 3. Parse the data
    args = parser.parse_args()

    # --- INTRO PART START ---
    print("--------------------Welcome to Binance Futures Testnet USDT-M Bot Service---------------- \n")
    print("\n")
    
    # Using the symbol from the arguments for print statement
    currency_symbol = args.symbol.upper()
    print(f"Target Symbol: {currency_symbol}")
    # --- INTRO PART END ---

    # Validation & Execution
    if validate_symbol(currency_symbol):
        trade_type = args.type.upper()
        
        if validate_trade_option(trade_type):
            trade_side = args.side.upper()
            
            if trade_side == 'BUY':
                # Passing all 4 values to new function structure
                buy_the_order(currency_symbol, trade_type, args.qty, args.price,args.stopprice)
                
                
            elif trade_side == 'SELL':
                sell_the_order(currency_symbol, trade_type, args.qty, args.price,args.stopprice)
    else:
        print(f"Validation Failed for {currency_symbol}")

if __name__ == "__main__":
    main()
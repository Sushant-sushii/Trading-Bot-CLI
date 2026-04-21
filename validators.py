from client import get_binance_client
 

client = get_binance_client()

try:
    # Fetching the account info response
    account_info = client.futures_account()
    positions = account_info.get('positions', [])

    all_symbol=[]
    for items in positions:
        symbol=items['symbol']
        all_symbol.append(symbol)
    # print(all_symbol)

    
   
except Exception as e:
    print(f"Error fetching account info: {e}")

def validate_symbol(currency_symbol):
    for symbol in all_symbol:
        if(currency_symbol==symbol):
            return True        
    return False

def validate_trade_option(trade_options):
    if trade_options in ["MARKET","LIMIT",'STOP_LIMIT']:
        return True
    return False
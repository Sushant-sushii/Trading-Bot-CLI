from client import get_binance_client
import logging
import time



client=get_binance_client()

# Buying Option
def buy_the_order(currency_symbol, trade_options, qty, price=None,stop_price=None):
   
    
    # MARKET Option
    if trade_options == 'MARKET':
        try:
            order = client.futures_create_order(
                symbol=currency_symbol.upper(),
                side='BUY',
                type='MARKET', 
                quantity=float(qty),
            )
            print(f"🔄 Connecting to Binance Testnet... [Symbol: {currency_symbol}]")
            time.sleep(0.5)
            msg = f"Market BUY Success: {currency_symbol} | Qty: {qty} | OrderID: {order['orderId']} |Status :{order['status']} | AveragePrice : {order['avgPrice']}"
            print(f"Congratulations! {msg}")
            logging.info(msg)   

            args_summary = {
            'symbol': currency_symbol,
            'type': trade_options,
            'qty': qty,
            'price': price
            }     
             
            return order,args_summary
        except Exception as e:
            err_msg = f"Market Order Failed: {e}"
            print(f"Oops! {err_msg}")
            logging.error(err_msg)
            return None
    # LIMIT Option
    elif trade_options == 'LIMIT':
        
        try:         
            order = client.futures_create_order(
                symbol=currency_symbol.upper(),
                side='BUY',
                type='LIMIT',
                quantity=float(qty),
                price=float(price),
                timeInForce='GTC' ,
            )
            msg = f"Limit BUY Success: {currency_symbol} | Price: {price} | Qty: {qty} | OrderID: {order['orderId']}|Status :{order['status']} | AveragePrice : {order['avgPrice']}"
            print(f"Congratulations! {msg}")
            logging.info(msg)
            return order
        except Exception as e:
            err_msg = f"Limit Order Failed: {e}"
            print(f"Oops! {err_msg}")
            logging.error(err_msg)
            return None
        
    # STOP-LIMIT buy Option
    elif trade_options =='STOP_LIMIT':        
        try:
            print(f"DEBUG: Entering STOP_LIMIT logic for {currency_symbol}")
            order = client.futures_create_order(
                symbol=currency_symbol.upper(),
                side='BUY',
                type='STOP',
                quantity=float(qty),
                price=float(price),           
                stopPrice=float(stop_price),   
                timeInForce='GTC'
            )
            orderID=order.get("orderId","Unknown")
            orderStatus=order.get('status',"New")
            orderAvgPrice=order.get('avgPrice',"Null")
            msg = f"Stop-Limit BUY Success: {currency_symbol} | Price: {price} | Qty: {qty} | OrderID: {orderID} |Status :{orderStatus} | AveragePrice : {orderAvgPrice}"
            print(f"Congratulations! {msg}")
            logging.info(msg)
            return order
        except Exception as e:
            print(f"Oops! Stop-Limit Failed: {e}")
            return None

    else:
        return "Please Choose Valid Option!"
    

# Sell Logic

def sell_the_order(currency_symbol, trade_options, qty, price=None,stop_price=None):
    symbol_upper = currency_symbol.upper()
    
    # Market Sell option
    if trade_options == 'MARKET':
        try:
            order = client.futures_create_order(
                symbol=symbol_upper,
                side='SELL', 
                type='MARKET',
                quantity=float(qty)
            )
            msg = f"Market SELL Success: {symbol_upper} | Qty: {qty} | OrderID: {order['orderId']}|Status :{order['status']} | AveragePrice : {order['avgPrice']}"
            print(f"Congratulations! {msg}")
            logging.info(msg)
            # checking order info
            # print(order.keys())

            return order
        except Exception as e:
            err_msg = f"Market SELL Failed: {e}"
            print(f"Oops! {err_msg}")
            logging.error(err_msg)
            return None
    # LIMIT Sell Option
    elif trade_options == 'LIMIT':
     
        try:         
            order = client.futures_create_order(
                symbol=symbol_upper,
                side='SELL', 
                type='LIMIT',
                quantity=float(qty),
                price=float(price),
                timeInForce='GTC'
            )
            msg = f"Limit SELL Success: {symbol_upper} | Price: {price} | Qty: {qty} | OrderID: {order['orderId']} |Status :{order['status']} | AveragePrice : {order['avgPrice']}"
            print(f"Congratulations! {msg}")
            logging.info(msg)
            return order
        except Exception as e:
            err_msg = f"Limit SELL Failed: {e}"
            print(f"Oops! {err_msg}")
            logging.error(err_msg)
            return None
    # STOP-LIMIT Sell Option
    elif trade_options == 'STOP_LIMIT':        
        try:
            order = client.futures_create_order(
                symbol=currency_symbol.upper(),
                side='SELL',
                type='STOP',
                quantity=float(qty),
                price=float(price),           
                stopPrice=float(stop_price),   
                timeInForce='GTC'
            )

            #extracting response and initializing fallbacks  
            orderID=order.get("orderId","Unknown")
            orderStatus=order.get('status',"New")
            orderAvgPrice=order.get('avgPrice',"Null")

            msg = f"Stop-Limit SELL Success: {currency_symbol} | Price: {price} | Qty: {qty} | OrderID: {orderID} |Status :{orderStatus} | AveragePrice : {orderAvgPrice}"
            print(f"Congratulations! {msg}")
            logging.info(msg)

            return order
        except Exception as e:
            print(f"Oops! Stop-Limit Failed: {e}")
            return None
    else:
        print("Invalid Sell Option!")
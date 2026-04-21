import os
import logging
from binance.client import Client
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    if not api_key or not api_secret:
        logging.error("API Keys missing in .env file")
        raise ValueError("API Keys missing. Please check your .env file.")

    # testnet=True is mandatory for this task [cite: 10, 11]
    client = Client(api_key, api_secret, testnet=True)
    return client
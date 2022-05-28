import requests
import pandas as pd
import pandas_datareader.data as web

from dotenv import load_dotenv

load_dotenv()

import os

API_KEY = os.getenv('API_KEY')
print(API_KEY)

def get_crypto_price(symbol):
    api_url = f'https://cloud.iexapis.com/stable/crypto/{symbol}/price?token={API_KEY}'
    raw = requests.get(api_url).json()
    price = raw['price']
    return float(price)


start = '1/1/2020'
end = '1/31/2022'
data = web.DataReader('btcusd', 'iex', start, end)

print(data)
    
#btc = get_crypto_price('btcusd')
#print('Price of 1 Bitcoin: {} USD'.format(btc))
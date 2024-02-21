import os
import math
import json
import time
import locale
import requests
from prettytable import PrettyTable

#locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

local_currency = 'INR'
local_symbol = '₹'

api_key = '35e0ac39-15d3-4d9d-b850-b94937e051f4'
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(global_url, headers=headers)
results = request.json()

#print(json.dumps(results, sort_keys=True, indent=4))

data = results["data"]

total_market_cap = int(data["quote"][local_currency]["total_market_cap"])
total_market_cap_string = '{:,}'.format(total_market_cap)

table = PrettyTable(['Name', 'Ticker', '% of Total Market Cap', 'Price', '10.9T (Gold)', '35.2T (Narrow Money)', '89.5T (Stock Markets)'])

listing_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

request = requests.get(listing_url, headers=headers)
results = request.json()

data = results['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']

    market_cap = currency['quote'][local_currency]['market_cap']

    percentage_of_global_cap = float(market_cap) / float(total_market_cap)

    price = currency['quote'][local_currency]['price']

    available_supply = currency['total_supply']

    #gold_price = 10900000000000 * percentage_of_global_cap / available_supply
    #narrow_money_price = 35200000000000 * percentage_of_global_cap / available_supply
    #stock_market_price = 89500000000000 * percentage_of_global_cap / available_supply

    percentage_of_global_cap_string = str(round(percentage_of_global_cap*100, 2)) + '%'
    price_string = local_symbol + '{:,}'.format(round(price,5))
    gold_price_string = local_symbol + '{:,}'.format(round(gold_price,2))
    narrow_money_price_string = local_symbol + '{:,}'.format(round(narrow_money_price,2))
    stock_market_price_string = local_symbol + '{:,}'.format(round(stock_market_price,2))

    table.add_row([name,ticker,percentage_of_global_cap_string,price_string,gold_price_string,narrow_money_price_string,stock_market_price_string])

print()
print(table)
print()
time.sleep(10)
os.system('cls')
os.system('python main.py')

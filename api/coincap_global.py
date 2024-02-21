import requests
import json

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

btc_dominance = data["btc_dominance"]
eth_dominance = data["eth_dominance"]
total_market_cap = data["quote"][local_currency]["total_market_cap"]
total_volume_24h = data["quote"][local_currency]["total_volume_24h"]

total_market_cap = round(total_market_cap, 2)
total_volume_24h = round(total_volume_24h, 2)
btc_dominance = round(btc_dominance, 2)
eth_dominance = round(eth_dominance, 2)

total_market_cap_string = local_symbol + '{:,}'.format(total_market_cap)
total_volume_24h_string = local_symbol + '{:,}'.format(total_volume_24h)

print()
print('The global market cap for all cryptocurrencies is ' + total_market_cap_string + ' and the total 24h value is ' + total_volume_24h_string + '.')
print('Bitcoin makes up ' + str(btc_dominance) + '% of the global market cap and the Ethereum makes up ' + str(eth_dominance) + '%.')

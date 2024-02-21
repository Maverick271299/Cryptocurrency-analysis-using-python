import os
import csv
import time
import json
import requests
from prettytable import PrettyTable
from colorama import Fore, Back, Style

local_currency = 'INR'
local_symbol = '₹'

api_key = '35e0ac39-15d3-4d9d-b850-b94937e051f4'
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("MY PORTFOLIO")
print()

portfolio_value = 0.00

table = PrettyTable(['Asset', 'Ammount Owned', 'Value', 'Price', '1h', '24h', '7d'])

with open("projects/project1/my_portfolio.csv", "r", encoding="utf-8-sig") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        if '\ufeff' in line[0]:
            line[0] = line[0][1:].upper()
        else:
            line[0] = line[0].upper()

        symbol = line[0]
        amount = line[1]

        quote_url = base_url +  '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol

        request = requests.get(quote_url, headers=headers)
        results = request.json()

        #print(json.dumps(results, sort_keys=True, indent=4))

        currency = results['data'][symbol]

        name = currency['name']

        quote = currency['quote'][local_currency]

        hour_change = round(quote['percent_change_1h'], 1)
        day_change = round(quote['percent_change_24h'], 1)
        week_change = round(quote['percent_change_7d'], 1)

        price = quote['price']

        value = float(price) * float(amount)

        portfolio_value += value

        if hour_change > 0:
            hour_change = Fore.BLACK + Back.GREEN + str(hour_change) + '%' + Style.RESET_ALL
        else:
            hour_change = Fore.BLACK + Back.RED + str(hour_change) + '%' + Style.RESET_ALL

        if day_change > 0:
            day_change = Fore.BLACK + Back.GREEN + str(day_change) + '%' + Style.RESET_ALL
        else:
            day_change = Fore.BLACK + Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change > 0:
            week_change = Fore.BLACK + Back.GREEN + str(week_change) + '%' + Style.RESET_ALL
        else:
            week_change = Fore.BLACK + Back.RED + str(week_change) + '%' + Style.RESET_ALL

        price_string = '{:,}'.format(round(price,5))
        value_string = '{:,}'.format(round(price,5))

        table.add_row([name + ' (' + symbol + ')',
                    amount,
                    local_symbol + value_string,
                    local_symbol + price_string,
                    str(hour_change),
                    str(day_change),
                    str(week_change)])

print(table)
print()

portfolio_value_string = '{:,}'.format(round(portfolio_value,2))
print('Total Portfolio Value: ' + Fore.BLACK + Back.GREEN + local_symbol + portfolio_value_string + Style.RESET_ALL)
print()
time.sleep(10)
os.system('cls')
os.system('python main.py')

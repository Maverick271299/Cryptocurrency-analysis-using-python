import os
import csv
import sys
import json
import time
import requests
from datetime import datetime
import pyttsx3
# import engineio #engineio module is not needed.

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)    # Aquí puedes seleccionar la velocidad de la voz
engineio.setProperty('voice',voices[0].id)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()

local_currency = 'INR'
local_symbol = '₹'

api_key = '35e0ac39-15d3-4d9d-b850-b94937e051f4'
headers = {'X-CMC_PRO_API_KEY': api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("ALERTS TRACKING...")
print()

already_hit_symbols = []

while True:
    with open("projects/project2/my_alerts.csv", "r", encoding="utf-8-sig") as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if '\ufeff' in line[0]:
                line[0] = line[0][1:].upper()
            else:
                line[0] = line[0].upper()
            symbol = line[0]
            amount =line[1]

            quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + '&symbol=' + symbol

            request = requests.get(quote_url, headers=headers)
            results = request.json()

            #print(json.dumps(results, sort_keys=True, indent=4))

            currency = results['data'][symbol]

            name = currency['name']
            price = currency['quote'][local_currency]['price']

            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                speak('ALERT ALERT ALERT')
                speak(name + ' hit ' + amount)
                sys.stdout.flush()

                now = datetime.now()
                current_time = now.strftime("%I:%M%p")
                print(name + ' hit ' + amount + ' at ' + current_time + '!')
                already_hit_symbols.append(symbol)

    print('...')
    time.sleep(10)
    csv_file.close()
    break
os.system('cls')
os.system('python main.py')

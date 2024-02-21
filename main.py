
import os

print()
# print("CoinMarketCap Explorer Menu")
# print()
print("""
-----------------------------------------------------------------------------------------------------------------

            CoinMarketCap Explorer Menu

           1.My Portfolio
           2.Alert System.
           3.Top 100 Cryptocurencies.
           5.Top 1000 Cryptocurencies in Excel Sheet.
           6.Specific Cryto Coin Details.
           0.Exit.
""")
print()

choice = input("What is your choice (1-5): ")

sort = ""

if choice == '1':
    sort = os.system('python projects/project1/portfolio.py')
if choice == '2':
    sort = os.system('python projects/project2/alerts.py')
if choice == '3':
    sort = os.system('python projects/project3/top100.py')
if choice == '4':
    sort = os.system('python projects/project5/excel_writer.py')
if choice == '5':
    sort = os.system('python projects/project6/specific.py')
if choice == '0':
    exit(0)

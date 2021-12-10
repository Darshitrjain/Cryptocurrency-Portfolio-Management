import os
import csv
import json
import requests
from prettytable import PrettyTable
from colorama import init, Fore, Back, Style

init(convert=True)

l_c = 'USD'
c_s = '$'

api_key = 'ENTER YOUR KEY'

headers = {'X-CMC_PRO_API_KEY' : api_key}

base_url = 'https://pro-api.coinmarketcap.com'

print()
print("My Holdings")
print()

pfolio_val=0.00

table =PrettyTable(['Coin','Amount Acquired','Value','Price','7d'])

with open ("crypto portfolio.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file)
    for i in csv_reader:
        i[0]=i[0].upper()
        amt=i[1]
        symb=i[0]

        call_url=base_url + '/v1/cryptocurrency/quotes/latest?symbol=' + symb

        r = requests.get(call_url, headers=headers)
        result = r.json()

        curr=result['data'][symb]
        name = curr['name']
        q= curr['quote'][l_c]
        wc = round(q['percent_change_7d'],1)
        price=q['price']

        val=float(price)*float(amt)

        pfolio_val+=val

        if wc>0:
            wc=Back.GREEN + str(wc)+ '%' + Style.RESET_ALL
        else:
            wc=Back.RED + str(wc)+ '%' + Style.RESET_ALL

        price_s='{:,}'.format(round(price,2))

        val_s='{:,}'.format(round(val,2))

        table.add_row([name + '('+ symb +')',
                       amt,
                       c_s + val_s,
                       c_s + price_s,
                       str(wc)])

print(table)

pfolio_s='{:,}'.format(round(pfolio_val,2))

print("TOTAL PORTFOLIO VALUE : "+Fore.BLACK +Back.GREEN +c_s+ pfolio_s+Style.RESET_ALL)

        #print(json.dumps(result, sort_keys=True, indent=4))

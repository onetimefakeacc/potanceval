#!/usr/bin/env python3
import os

f = open('transactions.txt')

# bypass charmap error on read() for some reason
txt = os.read(f.fileno(), 30*1024).decode('utf-8')
txt = txt.replace('\r', '').strip().split('\n')
txt = [[x for x in x.split('?') if x] for x in txt][1:]

# UserId TransactionId TransactionTime ItemCode ItemDescription NumberOfItemsPurchased CostPerItem

f = open('pack.csv', 'w+')
buf = ""

minprice = [str(10**10)] * 7

for item in txt:
    if 'набор' in item[4].lower():
        buf += item[4] + "?" + item[6] + "?\n"  # like "НАБОР ИЗ 12 ЦВЕТНЫХ КАРАНДАШЕЙ?72,0?", as in transactions.txt
        if float(item[6].replace(',', '.')) < float(minprice[6].replace(',', '.')):
            minprice = item

f.write(buf)

print(f"Самый дешевый товар в категории набор: {minprice[4]}, цена такого товара составит: {minprice[6]}")

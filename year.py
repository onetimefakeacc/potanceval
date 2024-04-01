#!/usr/bin/env python3
import os

f = open('transactions.txt')

# bypass charmap error on read() for some reason
txt = os.read(f.fileno(), 30*1024).decode('utf-8')
txt = txt.replace('\r', '').strip().split('\n')
txt = [[x for x in x.split('?') if x] for x in txt][1:]

# UserId TransactionId TransactionTime ItemCode ItemDescription NumberOfItemsPurchased CostPerItem


months = {}

for item in txt:
    m = item[2].split('.')[1]

    if m not in months:
        months[m] = []

    months[m].append(int(item[5]) * float(item[6].replace(",", ".")))

for m in months:
    avg = sum(months[m]) // len(months[m])
    count = len(months[m])
    months[m] = [count, avg]

s = sorted(months.items())

f = open('table.txt', 'w+')
buf = ""

for x in s:
    buf += str(x[0]) + " " + str(x[1][0]) + " " + str(x[1][1]).replace(".", ",") + "\n"

f.write(buf)
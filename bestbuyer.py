#!/usr/bin/env python3
import os

f = open('transactions.txt')

# bypass charmap error on read() for some reason
txt = os.read(f.fileno(), 30*1024).decode('utf-8')
txt = txt.replace('\r', '').strip().split('\n')
txt = [[x for x in x.split('?') if x] for x in txt][1:]

# UserId TransactionId TransactionTime ItemCode ItemDescription NumberOfItemsPurchased CostPerItem


users = {}

for item in txt:
    if item[0] == "-1":  # idk there is transactions with -1 user id
        continue

    if item[0] not in users:
        users[item[0]] = 0.0

    users[item[0]] += int(item[5]) * float(item[6].replace(",", "."))  # NumberOfItemsPurchased * CostPerItem 

best = sorted(users.items(), key=lambda x:x[1], reverse=True)[:7]

f = open('best_buyer.csv', 'w+')
buf = ""

for x in best:
    buf += x[0] + " " + str(round(x[1], 1)).replace(".", ",") + '\n'

f.write(buf)
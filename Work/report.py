# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint


def read_portfolio(filename):
    res = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            res.append({'name' : row[0], 'shares' : row[1], 'price' : row[2]})
    return res


def calc_gain(filename):
    res = ""
    p = read_portfolio(filename)
    v = {}
    with open('Data/prices.csv') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                v[row[0]] = row[1]
            except:
                pass
    
    # Original price
    cur = 0
    for row in p:
        cur += float(row['price']) * int(row['shares'])
    res += f"Original value: {cur}"

    # Gain/loss
    gain = 0
    for row in p:
        row['price'] = v[row['name']]
        gain += float(row['price']) * int(row['shares'])
    res += f"\nGain/loss: {cur - gain:0.2f}"

    return res


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

portfolio = read_portfolio(filename)
pprint(portfolio)

net = calc_gain(filename)
print(f"\n{net}")

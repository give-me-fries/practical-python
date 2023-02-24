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


def read_prices(filename):
    res = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                res[row[0]] = row[1]
            except:
                pass
    return res


def make_report(portfolio, prices):
    res = ""
    table = []
    for i in range(len(portfolio)):
        table.append((
            portfolio[i]['name'],
            int(portfolio[i]['shares']),
            float(prices[portfolio[i]['name']]),
            round(float(prices[portfolio[i]['name']])-float(portfolio[i]['price']),2)
            ))
    
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f"{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print("---------- ---------- ---------- -----------")
    for name, shares, price, change in table:
        price = "$" + str(round(price,2)) 
        print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")

    return table


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

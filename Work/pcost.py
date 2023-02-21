# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print("Cannot parse", row)
    return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

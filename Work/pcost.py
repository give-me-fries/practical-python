# pcost.py
#
# Exercise 1.27
import csv
import sys
import report


def portfolio_cost(filename):
    return sum(stock['shares'] * stock['price'] for stock in report.read_portfolio(filename))


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

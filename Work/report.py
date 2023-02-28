# report.py
#
# Exercise 2.4

import csv
import fileparse


def read_portfolio(filename):
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
                'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    '''
    return fileparse.parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(filename):
    '''
    prices = {}
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                pass
    '''
    return dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


def print_report(report):
    res = ''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- ----------')
    for name, share, price, change in report:
        print('%10s %10s %10s %10.2f' % (
            name, share, '$' + str(price), change
        ))


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)


portfolio_report('Data/portfolio.csv', 'Data/prices.csv')

import csv
import fileparse

def read_portfolio(lines):
    return fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(lines):
    return dict(fileparse.parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


def print_report(report):
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


def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s <portfolio file> <prices file>' % args[0])
    portfolio_report(args[1], args[2])


if __name__ == '__main__':
    import sys
    main(sys.argv)

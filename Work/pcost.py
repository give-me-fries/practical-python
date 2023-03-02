# pcost.py
#
# Exercise 1.27
import csv
import sys
import report


def portfolio_cost(filename):
    return sum(stock['shares'] * stock['price'] for stock in report.read_portfolio(filename))


def main(args):
    if len(args) != 2:
        raise SystemExit('Usage: %s <portfolio file>' % args[0])
    print('Total cost:', portfolio_cost(args[1]))


if __name__ == '__main__':
    import sys
    main(sys.argv)

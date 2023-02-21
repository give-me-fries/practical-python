# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        headers = next(f)
        for row in f:
            line = row.split(',')
            try:
                total += int(line[1]) * float(line[2])
            except ValueError:
                print("Cannot parse", line)
    return total

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
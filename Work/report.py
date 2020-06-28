# report.py:q
#
# Exercise 2.4


import csv
from pprint import pprint

def read_prices(filename):
    prices = {}
    try:
        with open(filename,'r') as f:
            rows = csv.reader(f)
            for row in rows:
                if len(row) == 0:
                    continue
                (name, price) = row
                prices[name] = float(price)
    except FileNotFoundError:
        print('File not found', filename)
    return prices

def read_portfolio2(filename):
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)

            select = ['name', 'shares', 'price']
            indices = [headers.index(colname) for colname in select]
            portfolio = [ { colname: row[index] for colname, index in zip(select, indices) } for row in rows ]
            return portfolio
    except FileNotFoundError:
        print('File not found')
        return None

def read_portfolio(filename):
    portfolio = []
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            header = next(rows)
            for rowno, row in enumerate(rows, start=1):
                record = dict(zip(header,row))
                try:
                    name = record['name']
                    qty = int(record['shares'])
                    price = float(record['price'])
                    portfolio.append({'name': name, 'shares': qty, 'price': price})
                except ValueError:
                    print(f'invalid record on rowno {rowno} - skipping entry: {row}')
        return portfolio
    except FileNotFoundError:
        print('File not found')
        return None

def read_portfolio3(filename):
    portfolio = []
    types = [str, int, float]
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            header = next(rows)
            for rowno, row in enumerate(rows, start=1):
                converted = [func(val) for func, val in zip(types, row)]
                record = dict(zip(header,converted))
                
                try:
                    name = record['name']
                    qty = int(record['shares'])
                    price = float(record['price'])
                    portfolio.append({ name: func(val) for name, func, val in zip(header, types, row) })
                except ValueError:
                    print(f'invalid record on rowno {rowno} - skipping entry: {row}')
        return portfolio
    except FileNotFoundError:
        print('File not found')
        return None

def make_report(portfolio, prices):
    report=[]
    for s in portfolio:
        if s['name'] in prices:
            diff = (prices[s['name']] - s['price'])
        else:
            diff = None
        report.append((s['name'], s['shares'], prices[s['name']], diff))
    return report


def print_report(report):
    def header_formatting(name):
        return f"{name:>10s}"

    headers = ('Name', 'Shares', 'Price', 'Change')
    print(' '.join(map(header_formatting, headers)))
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        price_value = f"${price:.2f}"
        price_with_currency = f"{price_value:>10s}"
        print(f'{name:>10s} {shares:>10d} {price_with_currency} {change:>10.2f}')

#Reading and type-casting data files
def test_func_casts():
    f = open('Data/dowstocks.csv')
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)
    types = [str, float, lambda x: tuple(x.split('/')), str, float, float, float, float, int]
    converted = [func(val) for func, val in zip(types, row)]
    record = dict(zip(headers, converted))
    print(record)

def example_of_counter(portfolio):
    from collections import Counter
    total_shares = Counter()
    for record in portfolio:
        total_shares[record['name']] += record['shares']

    print(total_shares)

def example_of_comprehensions(portfolio):
    sum_using_comprehension = sum([s['shares']*s['price'] for s in portfolio])

    current_value_of_portfolio = sum([s['shares']*prices[s['name']] for s in portfolio])
    print(current_value_of_portfolio)

    msftibm = [ s for s in portfolio if s['name'] in {'MSFT','IBM'} ]

    names_using_set_comprehension = { s['name'] for s in portfolio }
    print(names_using_set_comprehension)

    portfolio_prices_dict_comprehension = { name: prices[name] for name in names_using_set_comprehension }
    print(portfolio_prices_dict_comprehension)


def portfolio_report(portfolio_filename, prices_filename):
    prices = read_prices(prices_filename)
    #pprint(prices)

    #portfolio = read_portfolio('Data/missing.csv')
    portfolio = read_portfolio(portfolio_filename)
    #pprint(portfolio)

    report = make_report(portfolio, prices)

    print_report(report)


portfolio_report('Data/portfoliodate.csv','Data/prices.csv')

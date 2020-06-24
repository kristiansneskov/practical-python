# report.py
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
    print('---------- ---------- ---------- -----------')
    for name, shares, price, change in report:
        price_value = f"${price:.2f}"
        price_with_currency = f"{price_value:>10s}"
        print(f'{name:>10s} {shares:>10d} {price_with_currency} {change:>10.2f}')

prices = read_prices('Data/prices.csv')
#pprint(prices)

#portfolio = read_portfolio('Data/missing.csv')
portfolio = read_portfolio('Data/portfoliodate.csv')
#pprint(portfolio)

report = make_report(portfolio, prices)

print_report(report)


#total=0
#total_diff = 0
#for s in portfolio:
#    total += s['shares'] * s['price']
#    if s['name'] in prices:
#        diff = round(s['shares'] * (s['price'] - prices[s['name']]),2)
#        if diff >= 0:
#            text = str.ljust(f"Total gain on {s['name']}" ,20)
#            print(f"{text} = {diff:>10.2f}")
#        else:
#            text = str.ljust(f"Total loss on {s['name']}" ,20)
#            print(f"{text} = {diff:>10.2f}")
#        total_diff += diff
#    else:
#        print(f"No price for share {s['name']}")
#print(total)
#diff_text = 'gain' if total_diff > 0 else 'loss'
#print(f"Total {diff_text} = {round(total_diff,2)}")


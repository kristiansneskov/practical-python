# pcost.py
#
# Exercise 1.27


import os
import csv

def portfolio_cost(filename):
    try:
        with open(filename, 'rt') as f:
            rows = csv.reader(f)
            header = next(rows)
            sum = 0
            for rowno, row in enumerate(rows, start=1):
                record = dict(zip(header,row))
                try:
                    qty = int(record['shares'])
                    price = float(record['price'])
                    sum = sum + int(qty) * float(price)
                except ValueError:
                    print(f'Row {rowno}: Could not convert: {row} - skipping entry')
        return sum
    except FileNotFoundError:
        print('File not found')
        return None

cost = portfolio_cost('Data/portfoliodate.csv')
print('Total cost:', cost)


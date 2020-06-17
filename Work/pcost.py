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
            for row in rows:
                (name,qty,price) = row
                try:
                    sum = sum + int(qty) * float(price)
                except ValueError:
                    print(f'invalid record encountered on line:{row} - skipping entry')
        return sum
    except FileNotFoundError:
        print('File not found')
        return None

cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)


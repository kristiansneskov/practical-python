# fileparse.py
#
# Exercise 3.3
# fileparse.py


import csv

def parse_csv(filename, select = [], types = [], has_headers = True, delimiter = ',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        # Read the file headers
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
        else:
            indices = []

        records = []
        for index,row in enumerate(rows, start=1):
            if not row:    # Skip rows with no data
                continue
            if indices:
                row = [ row[index] for index in indices]
            #row = [ row[index] for index in indices]

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {index}: Could not convert {row}")
                        print(f"Row {index}: {e}")
            #record = {colname: row[index] for colname, index in zip(select, indices)}
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

    return records

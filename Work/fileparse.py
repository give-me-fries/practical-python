# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(
        filename,
        select=None,
        types=None,
        has_headers=True,
        delimiter=",",
        silence_errors = False
):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        
        if select and not has_headers:
            raise RuntimeError("select argument requires column headers")

        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        if has_headers:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting ditionaries.
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        
        records = []
        for rowNum, row in enumerate(rows, start=1):
            try:
                if not row:    # Skip rows with no data
                    continue
                # Filter the row if specifc columns were selected
                if indices:
                    row = [row[index] for index in indices]
                if types:
                        row = [func(val) for func, val in zip(types, row)]
                # Make a dictionary
                if has_headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(
                        f"Row {rowNum}: Couldn't convert {row}\n"
                        f"Row {rowNum}: {e}"
                    )


    return records

import csv

def parse_csv(
        lines,
        select=None,
        types=None,
        has_headers=True,
        delimiter=",",
        silence_errors=False
):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    # Open file if user inputted file, otherwise parse info as normal
    isFile = False
    if type(lines) == str:
        isFile = True
        f = open(lines)
        rows = csv.reader(f, delimiter=delimiter)
    else:
        rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers
    if has_headers:
        headers = next(rows)
    else:
        headers = []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting ditionaries.
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select
    
    records = []
    for rowNum, row in enumerate(rows, start=1):
        if not row:    # Skip rows with no data
            continue
        
        # Filter the row if specifc columns were selected
        if select:
            row = [row[index] for index in indices]
        
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(
                        f"Row {rowNum}: Couldn't convert {row}\n"
                        f"Row {rowNum}: {e}"
                    )

        # Make a dictionary
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    
    if isFile:
        f.close()
    
    return records

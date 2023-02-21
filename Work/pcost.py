# pcost.py
#
# Exercise 1.27

total = 0
with open("Data/portfolio.csv", "rt") as f:
    headers = next(f)
    for line in f:
        row = line.split(",")
        total += int(row[1]) * float(row[2])

print(f"Total cost {total}")

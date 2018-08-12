import os
import csv

# Variables to track
date = []
revenue = []

# Read Files
with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # skip the header row.
    csv_header = next(csvfile)
    for row in csvreader:
        date.append(row[0])
        # read as string; convert to integer.
        revenue.append(int(row[1]))
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total Revenue: ${sum(revenue)}")

revChange = []
# revenue change starts with 2nd value.
# Loop through all the rows of data we collect
for i in range(1, len(revenue)):
    revChange.append(revenue[i] - revenue[i-1])

print(f"Average Revenue Change: ${sum(revChange)/len(revChange)}")
# "date" list has 1 more value than "revCh" list.
print(f"Greatest Increase in Revenue: {date[revChange.index(max(revChange))+1]} (${max(revChange)})")
print(f"Greatest Decrease in Revenue: {date[revChange.index(min(revChange))+1]} (${min(revChange)})\n")

import os
import csv


date = []
revenue = []


with open("budget_data.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = next(csvfile)
    for row in csvreader:
        date.append(row[0])
        
        revenue.append(int(row[1]))
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total Revenue: ${sum(revenue)}")

revChange = []

for i in range(1, len(revenue)):
    revChange.append(revenue[i] - revenue[i-1])

print(f"Average Revenue Change: ${sum(revChange)/len(revChange)}")
print(f"Greatest Increase in Revenue: {date[revChange.index(max(revChange))+1]} (${max(revChange)})")
print(f"Greatest Decrease in Revenue: {date[revChange.index(min(revChange))+1]} (${min(revChange)})\n")

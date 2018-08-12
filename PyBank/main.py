import os
import csv

date = []
revenue = []

budgetcsv = os.path.join('budget_data.csv')

with open(budgetcsv, 'r') as csvfile:
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

output_file = os.path.join("budget_sum.txt") 

with open(output_file, "w") as txt_file:
    
    txt_file.write(f"Total Months: {len(date)}")
    txt_file.write('\n')
    txt_file.write(f"Total Revenue: ${sum(revenue)}")
    txt_file.write('\n')
    txt_file.write(f"Average Revenue Change: ${sum(revChange)/len(revChange)}")
    txt_file.write('\n')
    txt_file.write(f"Greatest Increase in Revenue: {date[revChange.index(max(revChange))+1]} (${max(revChange)})")
    txt_file.write('\n')
    txt_file.write(f"Greatest Decrease in Revenue: {date[revChange.index(min(revChange))+1]} (${min(revChange)})\n")
import os
import csv

#Path for budget data file
budget_data = os.path.join("Resources", "budget_data.csv")

#Variables
month_count = 0
net_total = 0
month_revenue = 0
last_month_revenue = 0
profit_change = 0
profit_changes = []
months = []

with open(budget_data, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skips header row
    csv_header = next(csv_reader)
    
    for csv_header in csv_reader:
        month_count +=1
        months.append(csv_header[0])
        month_revenue = int(csv_header[1])
        net_total = net_total + month_revenue
        if month_count > 1:
            profit_change = month_revenue - last_month_revenue
            profit_changes.append(profit_change)
        last_month_revenue = month_revenue

# analyze the month by month results
sum_rev_changes = sum(profit_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(profit_changes)
min_change = min(profit_changes)
max_month_index = profit_changes.index(max_change)
min_month_index = profit_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

new_average_change = round(average_change,2)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${net_total}")
print(f"Average Revenue Change: ${new_average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")
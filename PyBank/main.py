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

with open(budget_data,newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        #Skips header row
        csv_header = next(csv_reader,None)

        month_count = 1

        for csv_header in csv_reader:
                month_count += 1
                months.append(csv_header[0])
                net = int(csv_header[1])
                net_total = net_total + net

                if month_count > 1:
                        profit_change = month_revenue - last_month_revenue
                        profit_changes.append(profit_change)
                last_month_revenue = month_revenue

sum_profit_changes = sum(profit_changes)
avg_change = sum_profit_changes / (month_count-1)


print(f"Total Months: {str(month_count)}")
print(f"Total of Profit/Losses: ${net_total}")
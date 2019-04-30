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

#Used to round average revenue change to 2 decimal places
new_average_change = round(average_change,2)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${net_total}")
print(f"Average Revenue Change: ${new_average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

#Text file output path
analysis_text_file = os.path.join("Financial Analysis.txt")

#Creating text file with analysis results
#Using \n to clean up and create 7 lines of text in text file otherwise
#it would show as single line
with open(analysis_text_file, 'w') as x:
    x.write("Financial Analysis" +"\n")
    x.write("----------------------------"+"\n")
    x.write(f"Total Months: {month_count}"+"\n")
    x.write(f"Total Revenue: ${net_total}"+"\n")
    x.write(f"Average Revenue Change: ${new_average_change}"+"\n")
    x.write(f"Greatest Increase in Revenue: {max_month} (${max_change})"+"\n")
    x.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})"+"\n") 

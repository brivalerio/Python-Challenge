import os
import csv

#Path for budget data file
budget_data = os.path.join("Resources", "budget_data.csv")

#Variables
month_count = 0
net_total = 0

with open(budget_data,newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        #Skips header row
        csv_header = next(csv_reader,None)

        month_count = 1

        for csv_header in csv_reader:
                month_count += 1

                net = int(csv_header[1])
                net_total = net_total + net


print(f"Total Months: {str(month_count)}")
print(f"Total of Profit/Losses: ${net_total}")
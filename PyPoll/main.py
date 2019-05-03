import os
import csv

#Path for election data file
election_data = os.path.join("Resources", "election_data.csv")

#Variables
vote_count = 0

with open(election_data, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    for csv_header in csv_reader:
        vote_count += 1


print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")




#Text file output path
#analysis_text_file = os.path.join("Election Results.txt")

#Creating text file with election results
#Using \n to clean up and create 9 lines of text in text file otherwise
#it would show as single line
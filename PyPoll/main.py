import os
import csv

#Path for election data file
election_data = os.path.join("Resources", "election_data.csv")

#Variables
vote_count = 0
votes = []
candidates = []


with open(election_data, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Skips header row
    csv_header = next(csv_reader)

    #Finding total vote counts and votes for each condidate from data file
    for csv_header in csv_reader:
        vote_count += 1
        candidate_name = csv_header[2]

        #Counting votes same candidate
        if candidate_name in candidates:
            candidate_index = candidates.index(candidate_name)
            votes[candidate_index] = votes[candidate_index] +1
        
        #Otherwise, creating new candidate name in list
        else:
            candidates.append(candidate_name)
            votes.append(1)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")

print("-------------------------")

print("-------------------------")

#Text file output path
#analysis_text_file = os.path.join("Election Results.txt")

#Creating text file with election results
#Using \n to clean up and create 9 lines of text in text file otherwise
#it would show as single line
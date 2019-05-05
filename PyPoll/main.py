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

#Finding vote % for each condidate
#Adding new variables here to make it easier to keep track of
percentage = []
max_vote = votes[0]
max_index = 0

for count in range(len(candidates)):
    vote_percent = votes[count]/vote_count * 100
    percentage.append(vote_percent)

    if votes[count] > max_vote:
        max_vote = votes[count]
        print(max_vote)
        max_index = count

winner = candidates[max_index]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {round((percentage[count]),3)}% ({votes[count]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Text file output path
#analysis_text_file = os.path.join("Election Results.txt")

#Creating text file with election results
#Using \n to clean up and create 9 lines of text in text file otherwise
#it would show as single line
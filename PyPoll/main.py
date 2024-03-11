#import modules for cross-OS functionality and file reading
import os
import csv

#CSV file path
csvpath = os.path.join("Resources", "election_data.csv")

#read in CSV
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
    
        #store header
        csv_header = next(csvreader)
    
        #lists to hold candidates by vote and unique candidates
        votes = []
        candidates = []
        
        #iterate through each row after the header to add to votes list:
        for row in csvreader:
                votes.append(row[2])
        
        #calculate the total number of votes cast
        total_votes = len(votes)
        
        #calculate a complete list of candidates who received votes
        for i in votes:
                if i not in candidates:
                        candidates.append(i)
        
        #count votes by candidate
        votes_cand0 = votes.count(candidates[0])
        votes_cand1 = votes.count(candidates[1])
        votes_cand2 = votes.count(candidates[2])
        
        #percentage of total vote by candidate
        per_cand0 = round(((votes_cand0/total_votes)*100), 3)
        per_cand1 = round(((votes_cand1/total_votes)*100), 3)
        per_cand2 = round(((votes_cand2/total_votes)*100), 3)

        #winner by popular vote by returning dictionary key with the highest value
        votes_dict = {candidates[0]: votes_cand0, candidates[1]: votes_cand1, candidates[2]: votes_cand2}
        winner = max(votes_dict, key=votes_dict.get)

        #Print results to terminal
        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {total_votes}")
        print("-------------------------")
        print(f"{candidates[0]}: {per_cand0}% ({votes_cand0})")
        print(f"{candidates[1]}: {per_cand1}% ({votes_cand1})")
        print(f"{candidates[2]}: {per_cand2}% {votes_cand2})")
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")
        
#The open() and writelines() functions create a text file and write the results to separate lines
#BEWARE that this code block WILL overwrite an existing file of the same name and location!
file = open("analysis/PyPollAnalysis.txt", "w")
results = ["Election Results \n",
        ("------------------------- \n"),
        (f"Total Votes: {total_votes} \n"),
        ("------------------------- \n"),
        (f"{candidates[0]}: {per_cand0}% ({votes_cand0}) \n"),
        (f"{candidates[1]}: {per_cand1}% ({votes_cand1}) \n"),
        (f"{candidates[2]}: {per_cand2}% {votes_cand2}) \n"),
        ("------------------------- \n"),
        (f"Winner: {winner} \n"),
        ("-------------------------")
        ]
file.writelines(results)
file.close()
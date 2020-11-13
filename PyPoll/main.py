# Modules
import os
import csv

# Path
# csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

csvpath = "election_data.csv"
print(csvpath)  

# Variables
total_votes = 0
vote_list = []
percent_list = []
candidate_list = []
candidates = ""
winner = ""

# Open csv
with open (csvpath, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        # count total number of votes
        total_votes = total_votes + 1 

        if row[2] not in candidate_list: 
            candidate_list.append(row[2])
            vote_list.append(1)
        else:
            vote_list[candidate_list.index(row[2])] += 1
    
    print(total_votes)
    print(candidate_list)
    print(vote_list)

   # Percentage of votes
    for x in vote_list:
        percent_list = [(x/total_votes) * 100, 1]
    print(percent_list)

# Winner
winner = candidate_list[vote_list.index(max(vote_list))]
print(winner)

# Print
print("Election Results")
print("......................")
print("Total Votes:" + str(total_votes))
print("......................")
for x in candidate_list:
    print(x + ": " + str(format(percent_list[candidate_list.index(x)], '.2f')) 
        + "% (" + str(vote_list[candidate_list.index(x)]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# Write to text file
f = open("output.txt", "w")
f.write("Election Results" + "\n")
f.write("....................." + "\n")
f.write("Total Votes:" + str(total_votes) + "\n")
f.write("....................." + "\n")
for x in candidate_list:
    f.write(x + ": " + str(format(percent_list[candidate_list.index(x)], '.2f')) 
        + "% (" + str(vote_list[candidate_list.index(x)]) + ")\n")
f.write("-------------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-------------------------\n")

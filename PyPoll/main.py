import csv
import os

total_votes=0
candidates=[]
candidate_votes={}

csv_file_path=os.path.join("Resources","election_data.csv")

with open(csv_file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    for row in csvreader:
        total_votes+=1
        
        candidate=row[2]
        # If the candidate is not in the list, add them
        if candidate not in candidates:
            candidates.append(candidate)
            
            candidate_votes[candidate]=0
        # add to the candidate's vote count
        candidate_votes[candidate]+=1

        # Print the election results header
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# variables for the winner
winner = ""
winner_votes = 0

# Calculate and print the results for each candidate
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # find the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes
        


# Print the election results header
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Output file path
output_file_path = os.path.join("analysis","election_result.txt")
 # Write the results to a text file
with open(output_file_path, 'w') as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("----------------------------\n")
    for candidate in candidates:
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------\n")



print("Results written to", output_file_path)                      
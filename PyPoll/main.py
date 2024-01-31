import os
import csv

# Creating path for file
csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Reading file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Iterateing through each row in the CSV file
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # Updateing the dictionary to keep track of votes for each candidate
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Printing the results to the console
print("Election Results")
print("")
print("-------------------------")
print("")
print(f"Total Votes: {total_votes}")
print("")
print("-------------------------")

for candidate, votes in candidates.items():
    percentage_votes = (votes / total_votes) * 100
    print("")
    print(f"{candidate}: {percentage_votes:.3f}% ({votes})")
    print("")

    if votes > winner["votes"]:
        winner["name"] = candidate
        winner["votes"] = votes

print("-------------------------")
print("")
print(f"Winner: {winner['name']}")
print("")
print("-------------------------")

# Writeing the results to a text file
output_file_path = 'analysis/election_results.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write("Election Results\n")
    print("")
    output_file.write("-------------------------\n")
    print("")
    output_file.write(f"Total Votes: {total_votes}\n")
    print("")
    output_file.write("-------------------------\n")

    for candidate, votes in candidates.items():
        percentage_votes = (votes / total_votes) * 100
        output_file.write(f"{candidate}: {percentage_votes:.3f}% ({votes})\n")

    output_file.write("-------------------------\n")
    print("")
    output_file.write(f"Winner: {winner['name']}\n")
    print("")
    output_file.write("-------------------------\n")

print("")
print(f"Results have been written to {output_file_path}")
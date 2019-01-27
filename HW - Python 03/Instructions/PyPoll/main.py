import os
import csv


orignal_file = os.path.join("Resources", "election_data.csv")
output_file = os.path.join("Results", "election_analysis.txt")

vote_count = 0

candidates = []
total_votes = {}

winning_candidate = ""
winning_count = 0


with open(orignal_file) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:
        vote_count = vote_count + 1
        candidate_name = row[2]
        
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            total_votes[candidate_name] = 0

        total_votes[candidate_name] = total_votes[candidate_name] + 1

with open(output_file, "w") as results_file:
    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_count}\n"
        f"-------------------------\n")
    print(results, end="")

    results_file.write(results)

    for candidate in total_votes:

        votes = total_votes.get(candidate)
        vote_percentage = float(votes) / float(vote_count) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        vote_details = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(vote_details, end="")

        results_file.write(vote_details)

    winning_details = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_details)

    results_file.write(winning_details)

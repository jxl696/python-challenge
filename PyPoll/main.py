import os
import csv

pollpath = os.path.join("election_data.csv")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

with open(pollpath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row["Candidate"]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    totalvotes = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(totalvotes, end="")

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

poll_summary = os.path.join("poll_summary.txt")
with open(poll_summary, "w") as txt_file:
        txt_file.write(totalvotes)
        txt_file.write(voter_output)
        txt_file.write(winning_candidate_summary)
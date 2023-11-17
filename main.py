import os
import csv
from collections import Counter

election_file = r'C:\Users\Adda\OneDrive\Bootcamp\Class Folder\Module 3\3 Challenge\python-challenge-1\Starter_Code\PyPoll\Resources\election_data.csv'

with open(election_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    rows = list(csvreader)

def election_analysis(rows):
    votes = len(rows)
    candidates = [row[2] for row in rows]
    candidate_stats_list = []
    max_votes = 0
    winner = ""

    for candidate in set(candidates):
        count = candidates.count(candidate)
        percentage = (count / votes) * 100
        candidate_stats = f"{candidate}: {percentage: .3f}% ({count})"
        candidate_stats_list.append(candidate_stats)

        if count > max_votes:
            max_votes = count
            winner = candidate

    print("Election Results:")
    print(f"Total Votes: {str(votes)}")

    for stats in candidate_stats_list:
        print(f"{str(stats)}")
    print(f"Winner: {str(winner)}")

    with open("ElectionAnalysis.txt", "w") as f:
        print("Election Results:", file=f)
        print("-------------------", file=f)
        print(f"Total Votes: {str(votes)}", file=f)
        print("-------------------", file=f)
        for stats in candidate_stats_list:
            print(f"{str(stats)}", file=f)
        print("-------------------", file=f)
        print(f"Winner: {str(winner)}", file=f)
        print("-------------------", file=f)

election_analysis(rows)
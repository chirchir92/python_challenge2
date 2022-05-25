# import dependencies
import os
import csv

# declare path to retrieve the csv
election = os.path.join("PyPoll/Resources/election_data.csv")

# open the dataset
with open(election, "r") as csvfile:
    electionfile = csv.reader(csvfile, delimiter=",")
    header = next(electionfile)

# initiate empty lists to to append data to
    totalvotes = []
    candidates =[]
    unique_candidates = []
    percent = []

    # set the count to zero before iterating through the data
    count = 0

    for row in electionfile:
        count = count + 1
        
        # append candidates names to the set list
        candidates.append(row[2])

    


import os
import csv
from pathlib import Path

#Join the path to collect the data from
election_csv = Path('/Users/amaramh/Desktop/Analysis Projects/Python-Challenge/PyPoll/Resources/election_data copy.csv')

#Set Variables
votecount = 0 
candidates = []
candidatelist = []
totalvotes = []
indvotes = []



#Open & read file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvfile)

    #print(header)

    #Read through each row & list candidate names
    for row in csvreader:

        #Total number of votes
        votecount = votecount + 1

        #List of candidates who received votes
        candidatelist.append(row[2])

        #Unique Names of Candidates
        def uniquecandidates(candidatelist): 
            unique = []
            for candidate in candidatelist:
                if candidate in unique:
                    continue
                else:
                    unique.append(candidatelist)
            return unique
        print(uniquecandidates(candidatelist))
        
        









       

    









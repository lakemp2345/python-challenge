import csv
import os
from typing import Text

totalvotes=0
candidates=[]
candidatevotes={}

csvpath = os.path.join('Resources', 'election_data.csv')
#csvFile="election_data.csv"
# Open current election CSV
with open(csvpath) as csvfile:

    electiondata=csv.reader(csvfile)

# Skip headers
    header = next(electiondata, None)
    print(header)
   
    
    for row in electiondata:
        print(row[2])
        totalvotes += 1
        candidatename=row[2]
        if candidatename not in candidates:
            candidates.append(row[2])
            candidatevotes[row[2]]= 0

        candidatevotes[row[2]]+= 1    
    print(candidatevotes)

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
inputFile = os.path.join("Resources", "election_data.csv")  # Input file path
fileOutput = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
totalVotes = 0  # Variable that holds the total number of votes
candidates = [] # list that holds the candidates in poll
candidateVotes = {} # dictionary that will hold the votes for each candidate receives
winningCount = 0 # variable that holds the winning counts
winningCandidate = "" #

# Read the csv file
with open(inputFile) as electionData:
    # create the csv reader
    csvreader = csv.reader(electionData)

    # read the header
    header = next(csvreader)

    # rows will be lists
        # index 0 is the ballot ID
        # index 2 is the user's candidate choice

    # for each row
    for row in csvreader:
        # add on to the total votes
        totalVotes +=1 # same as totalVotes = totalVotes +1

        # check to see if the candidate is in the list of candidates
        if row[2] not in candidates:
            # if the candiddate is not in the list, add to the list
            candidates.append(row[2])

            # add the value to the dictionary as well
            # {"key": value}
            # start the count at 1 for the votes
            candidateVotes[row[2]] = 1

        else:
            # the candidate is in the list of candidates
            #  add a vote to the flavor count
            candidateVotes[row[2]] += 1

#print(candidateVotes)
voteOutput = ""

for candidates in candidateVotes:
    # get the vote count and the percentage of the votes
    votes = candidateVotes.get(candidates)
    votePct = (float(votes) / float(totalVotes)) * 100.00

    voteOutput += f"\t{candidates}: {votePct:.3f}% ({votes:,}) \n"
    
    # compare the votes to the winning count
    if votes > winningCount:
        # update the votes to be the new winning count
        winningCount = votes
        # update the winning candidate
        winningCandidate = candidates

winningCandidateOuput = f"Winner: {winningCandidate}\n--------------------------"

# create an output varaible to hold the output
output = (
    f"\n\nElection Results\n"
    f"--------------------------\n"
    f"Total Votes: {totalVotes:,} \n"
    f"--------------------------\n"
    f"{voteOutput} \n"
    f"-------------------------- \n"
    f"{winningCandidateOuput}\n"
)

print(output)

# print the results and export the data to a text file
with open(fileOutput, "w") as textFile:
    # write the output to the text file
    textFile.write(output)
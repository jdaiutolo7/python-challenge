import os
import csv

election_data = os.path.join(".\\PyPoll\Resources/election_data.csv")

# List variables and set initial values = 0
total_votes = 0 
diana_votes = 0
charles_votes = 0
raymon_votes = 0

# Creating dictionaries of the candidates' names and the variables of their vote counts
candidates = ["Diana DeGette", "Charles Casper Stockham", "Raymon Anthony Doane"]
votes = [diana_votes, charles_votes, raymon_votes]

# Open csv file, assign it to a variable, and then skip the header values
with open(election_data, encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",") 
    csvheader = next(csvreader)     

    # Creating a for loop to count the total votes as well as the votes for each candidate based on the amount of times their name appears
    for row in csvreader: 

        total_votes +=1
        if row[2] == "Diana DeGette": diana_votes +=1
        elif row[2] == "Charles Casper Stockham": charles_votes +=1
        elif row[2] == "Raymon Anthony Doane": raymon_votes +=1

# Calculating the percentages based on the total vote counts of each candidate
diana_percent = (diana_votes/total_votes) *100
charles_percent = (charles_votes/total_votes) * 100
raymon_percent = (raymon_votes/total_votes)* 100

# Zipping the two dictionaries together and assigning variables in order to find the winning candidate
candidates_and_votes = dict(zip(candidates,votes))
winning_candidate = max(candidates_and_votes, key=candidates_and_votes.get)

# Print
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes})")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes})")
print(f"-------------------------")
print(f"Winner: {winning_candidate}")
print(f"-------------------------")

# Assigning variable for text file and opening it
PyPoll_Analysis = os.path.join(".\\PyPoll\Analysis/pypoll_analysis.txt")

with open(PyPoll_Analysis,"w") as txtfile:
# Write on a txt file
    txtfile.write(f"Election Results \n")
    txtfile.write(f"------------------------- \n")
    txtfile.write(f"Total Votes: {total_votes} \n")
    txtfile.write(f"------------------------- \n")
    txtfile.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles_votes}) \n")
    txtfile.write(f"Diana DeGette: {diana_percent:.3f}% ({diana_votes}) \n")
    txtfile.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon_votes}) \n")
    txtfile.write(f"------------------------- \n")
    txtfile.write(f"Winner: {winning_candidate} \n")
    txtfile.write(f"------------------------- \n")
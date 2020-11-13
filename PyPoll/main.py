#import
import os
import csv

#import and output file and read CSV
file_to_output = os.path.join('analysis',"PyPoll_analysis.txt")
csvpath=os.path.join('.','Resources','election_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    #variables & lists
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []


    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    #total votes
    total_votes = (len(votes))

    #votes by candidate
    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)    
    
    #percent of total
    khan_percent = round(((khan_votes / total_votes) * 100), 2)
    correy_percent = round(((correy_votes / total_votes) * 100), 2)
    li_percent = round(((li_votes / total_votes) * 100), 2)
    otooley_percent = round(((otooley_votes / total_votes) * 100), 2)
    
    #Winner 
    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"    

output = (
    f"Election Results\n"
    f"----------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------\n"
    f"Kahn: {khan_percent}% ({khan_votes})\n"
    f"Correy: {correy_percent}% ({correy_votes})\n"
    f"Li: {li_percent}% ({li_votes})\n"
    f"O'Tooley: {otooley_percent}% ({otooley_votes})\n"
    f"----------------\n"
    f"Winner: {winner}\n"
    f"----------------\n"
)

print(output)

with open(file_to_output, "w") as txt_file:
   txt_file.write(output)  

   file_to_output 

#import modules for os and csv
import os
import csv

#set the path
election_data_path = "Resources/election_data.csv"

#Variables
count_of_votes = 0

#instruct python to read csv file
with open(election_data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    total_votes = []
    Khan_votes = []
    Correy_votes = []
    Li_votes = []
    OTooley_votes = []    
    
    #read each row of data
    for row in csvreader:
        
        total_votes.append(str(row[1]))
        
        if row[2] == "Khan":
            Khan_votes.append(str(row[2]))

        if row[2] == "Correy":
            Correy_votes.append(str(row[2]))
        
        if row[2] == "Li":
            Li_votes.append(str(row[2]))
        
        if row[2] == "O'Tooley":
            OTooley_votes.append(str(row[2]))              
                
    #The total number of votes cast
    total_vote_count = len(total_votes)
    print(total_vote_count)
    #Calculating total votes for each candidate
    Khan_total = len(Khan_votes)
    print(Khan_total)
    Correy_total = len(Correy_votes)
    print(Correy_total)
    Li_total = len(Li_votes)
    print(Li_total)
    OTooley_total = len(OTooley_votes)
    print(OTooley_total)

    #Calculating the percentage of votes each candidate won
    pct_Khan = (Khan_total / total_vote_count) * 100
    pct_Khan_rounded = round(pct_Khan, 2)
    print(pct_Khan_rounded)
    pct_Correy = (Correy_total / total_vote_count) * 100
    pct_Correy_rounded = round(pct_Correy, 2)
    print(pct_Correy_rounded)
    pct_Li = (Li_total / total_vote_count) * 100
    pct_Li_rounded = round(pct_Li, 2)
    print(pct_Li_rounded)
    pct_OTooley = (OTooley_total / total_vote_count) * 100
    pct_OTooley_rounded = round(pct_OTooley)
    print(pct_OTooley_rounded)
    

    
#Export File

    #Results
    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(total_vote_count))
    print("-----------------------")
    print("Khan: " + str(pct_Khan_rounded) + "% " + " (" + str(Khan_total) + ")")
    print("Correy: " + str(pct_Correy_rounded) + "% " + " (" + str(Correy_total) + ")")
    print("Li: " + str(pct_Li_rounded) + "% " + " (" + str(Li_total) + ")")
    print("O'Tooley: " + str(pct_OTooley_rounded) + "% " + " (" + str(OTooley_total) + ")")
    print("-----------------------")
    #print("Winner: " + str(election_winner))
    print("-----------------------")




#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
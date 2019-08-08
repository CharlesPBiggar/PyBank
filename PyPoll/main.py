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

    #read each row of data
    for row in csvreader:
        
        #The total number of votes cast
        count_of_votes +=1
        total_votes = count_of_votes

        #A complete list of candidates who received votes


        #The percentage of votes each candidate won


        #The total number of votes each candidate won


        #The winner of the election based on popular vote.
    
    print(total_votes)

#Export File


#output Layout
#As an example, your analysis should look similar to the one below:
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
#-------------------------

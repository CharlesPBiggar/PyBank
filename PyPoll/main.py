#import modules for os and csv
import os
import csv

#set the path
election_data_path = "Resources/election_data.csv"

#instruct python to read csv file
with open(election_data_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip header
    csv_header = next(csvreader)

    #read each row of data
    for row in csvreader:
        print(row)

#import modules for os and csv
import os
import csv

#set the path
budget_data_path = os.path.join("Resources", "budget_data.csv")
print(budget_data_path)

#Define Variables
count_of_months = 0
total_profits = 0
row_index_total_profits = 1

#instruct python to read csv file
with open(budget_data_path, 'r',newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header
    csv_header = next(csvreader)

    #read each row of data
    for row in csvreader:
        
        #Find Total # of months included in data set
        count_of_months +=1
        total_months = count_of_months
    
        #Find net total amount of "Profit/Losses"
        float_total_profits = float(row[row_index_total_profits])
        total_profits += float_total_profits
    
        #Find average changes in "Profit/Losses"
        

        #Find the greatest increase in profits (date & amount)


        #Find the greatest decrease in profits (date & amount)
    
    #Values
    print(total_months)
    print(total_profits)
    
    


#Export File 


#OUTPUT LAYOUT
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

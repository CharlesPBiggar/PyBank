#import modules for os and csv
import os
import csv

#set the path
budget_data_path = os.path.join("Resources", "budget_data.csv")

#instruct python to read csv file
with open(budget_data_path, 'r',newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    
    #skip header
    csv_header = next(budget_data)
    
    profits = []
    
    #read each row of data
    for row in budget_data:
        
        #add values for Profits/Losses column to profits list
        profits.append(int(row[1]))
    
    total_months = len(profits)
    
    #Find net total amount of "Profit/Losses"
    total_profits = sum(profits)
    
    #Find month to month changes in "Profit/Losses"
    change = [profits[i+1] - profits[i] for i in range(len(profits)-1)]
    #Find average of changes 
    avg_change = sum(change)/len(change)
    avg_change_rounded = round(avg_change, 2)
    
    #Find the greatest increase in profits (date & amount)
    greatest_increase = max(change)       
    
    #Find the greatest decrease in profits (date & amount)
    greatest_decrease = min(change)
        
    #Results
    print("Financial Analysis")
    print("--------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profits: $" + str(total_profits))
    print("Average Change: $" + str(avg_change_rounded))
    print("Greatest Increase in Profits: $" + str(greatest_increase))
    print("Greatest Decrease in Profits: $" + str(greatest_decrease))

#Export File 


#OUTPUT LAYOUT
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
#Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

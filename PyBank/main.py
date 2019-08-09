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
    print("---------------------------------------")
    print("Financial Analysis")
    print("---------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profits: $" + str(total_profits))
    print("Average Change: $" + str(avg_change_rounded))
    print("Greatest Increase in Profits: $" + str(greatest_increase))
    print("Greatest Decrease in Profits: $" + str(greatest_decrease))
    print("---------------------------------------")

# Export File
# Specify the file to write to
import os
import csv

output_path = os.path.join("Output", "Financial_Analysis.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the Title row
    csvwriter.writerow(["Total Months", "Total Profits", "Average Change", "Greatest Increase", "Greatest Decrease"])

    # Write the Results row
    csvwriter.writerow([str(total_months) + " Months", "$" + str(total_profits), "$" + str(avg_change_rounded), "$" + str(greatest_increase), "$" + str(greatest_decrease)])

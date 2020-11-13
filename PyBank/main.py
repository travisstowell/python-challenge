# PyBank
# Create a Python script that analyzes the records to calculate each of the following:

  # The total number of months included in the dataset
  # The net total amount of "Profit/Losses" over the entire period
  # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
  # The greatest increase in profits (date and amount) over the entire period
  # The greatest decrease in losses (date and amount) over the entire period
  # Print results to terminal and output file

#imports
import os
import csv

#variables & lists
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]   
change_list = []
monthly_profit_change = 0
months = [] 
total_months = 1
net_total= 0

#Output & Input
file_to_output = os.path.join('analysis',"PyBank_analysis.txt")
budget_csv = os.path.join('.','Resources','budget_data.csv')

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    first_row = next(csvreader)
    previous_row = int(first_row[1])
    net_total = int(first_row[1])
    
    for row in csvreader:

        net_total += int(row[1])
        total_months = total_months+1
        current_value = int(row[1])
        
        change_value = int(current_value-previous_row)

        change_list.append(change_value)
        months.append(row[0])
        previous_row = int(row[1])

        monthly_profit_change = monthly_profit_change + change_value 
        if change_value > greatest_increase[1]:
           greatest_increase[0] = str(row[0])
           greatest_increase[1] = change_value

        if change_value < greatest_decrease[1]:
           greatest_decrease[0] = str(row[0])
           greatest_decrease[1] = change_value
		
        avg_change = monthly_profit_change/len(months)
   
output = (
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: {net_total}\n"
    f"Average Revenue Change: ${avg_change}\n"
    f"Greatest increase in Revenue: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest decrease in Revenue: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
)

print(output)

with open(file_to_output, "w") as txt_file:
   txt_file.write(output)  

   file_to_output       

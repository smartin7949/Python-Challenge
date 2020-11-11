# Modules
import os
import csv

# Path
# csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

csvpath = "budget_data.csv"

print(csvpath)

# Variables
total_months = 0
total_revenue = []
months = []
revenue_change = []
monthly_profit_change = []
total_profit_loss= 0
prev_profit_loss = 0

# Open CSV
with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)

     # Read the header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # count total number of months
        total_months = total_months + 1 
        print(total_months)

    # find the net amount of profit and loss
    for rows in csvreader:
        total_revenue.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    for x in range(1, len(total_revenue)):
        revenue_change.append((int(total_revenue[x]) - int(total_revenue[x-1])))
    
    # calculate average revenue 
    revenue_average = sum(revenue_change) / len(revenue_change)   

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)

   # print the Results
    print("Financial Analysis") 
    print(".............................")

    print("Total Months: " + str(total_months))





    # Write to text file
    file = open("output.txt","w")
    file.write("Financial Analysis\n")
       


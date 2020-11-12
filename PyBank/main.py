# Modules
import os
import csv

# Path
# csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

csvpath = "budget_data.csv"

print(csvpath)

# Variables
total_revenue = []
months = []
total_months = 0
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

        
        # find the net amount of profit and loss
        total_revenue.append(int(row[1]))
        months.append(row[0])

    print(total_months)
    print(total_revenue)
    print(months)

    # find revenue change
    for x in range(1, len(total_revenue)):
        revenue_change.append((int(total_revenue[x]) - int(total_revenue[x-1])))
    
    print("rev change: ", revenue_change)

    # calculate average revenue 
    revenue_average = sum(revenue_change) / len(revenue_change)   

    print("rev average: ", revenue_average)

    greatest_increase = 0
    greatest_decrease = 0
    # greatest increase in revenue
    for y in revenue_change:
        if int(y) > greatest_increase:
            greatest_increase = y
        if int(y) < greatest_decrease:
            greatest_decrease = y
    
    print(greatest_increase)
    print(greatest_decrease)     
   

# print the Results
    print("Financial Analysis") 
    print(".............................")
    print("Total Months: " + str(total_months))
    print("Total:" + "$" + str(sum(total_revenue)))
    print("Average Change: " + "$", str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

# output to a text file

f = open("output.txt", "w")
f.write("Financial Analysis" + "\n")
f.write("..............................." + "\n")
f.write("Total Months: " + str(total_months) + "\n")
f.write("Average Change: " + "$" + str(revenue_average) + "\n")
f.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
f.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
f.close()

        


# Modules

import os
import csv

# Path
# csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

csvpath = "budget_data.csv"

print("you got here")

# Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
 
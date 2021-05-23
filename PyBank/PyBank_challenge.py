import csv
import os
output="analysis/"

total=0

csvpath= os.path.join('budget_data.csv')

# Open current budget CSV
with open(csvpath) as csvFile:
   
    budgetdata=csv.reader(csvFile)
    
# Skip headers
    header = next(budgetdata, None)
    Counter=0
    row1 = next(budgetdata)
    beginning = int(row1[1])
    
    for row in budgetdata:

        Counter= Counter + 1
        total= total + int(row[1])
    print(total)

    lastvalue=int(row[1])
    print(lastvalue)

    averagechange=(lastvalue-beginning)/Counter
    print(averagechange)
    # Calculate greatest increase and greatest decrease and append to the list
    

    output= "Financial Analysis"
    output= "total"
    output= "averagechange"


# Specify the file to write to
output_path=os.path.join("analysis", "budgetanalysis.txt")

output = (
    "data line\n"
    "data line 2"
)

# Open the file using "write" mode.  Specify the variable to hold the contents
with open(output_path, 'w', newline='') as text_file:
    text_file.write("some text here")
import csv
import os
from typing import Text
output="/Users/laurakemp/Documents/Homework/python-challenge/PyBank/analysis/budgetanalysis.txt"

totalNet=0
totalMonth=0
netchange=[]
monthYear=[]
greatestdecreasemonth=""
greatestincreasemonth=""
greatestdecrease=0
greatestincrease=0

csvpath = "/Users/laurakemp/Documents/Homework/python-challenge/PyBank/Resources/budget_data.csv"

# Open current budget CSV
with open(csvpath) as csvFile:
   
    budgetdata=csv.reader(csvFile)
    
# Skip headers
    header = next(budgetdata, None)
    totalMonth= totalMonth +1
    row1 = next(budgetdata)
    totalNet += int(row1[1])
    firstnet = int(row1[1])
    previousnet=firstnet
    
    for row in budgetdata:
        totalNet= totalNet + int(row[1])
        totalMonth += 1
        netchange.append(int(row[1])-previousnet)
        previousnet=int(row[1])
        monthYear.append(row[0])
    # Calculate greatest increase and greatest decrease and append to the list
    #for row in budgetdata:
    
    #print(row1)
    #print(netchange)
    averagechange=(previousnet-firstnet)/(totalMonth-1)
    print(totalMonth)
    print(totalNet)
    print(averagechange)
    #print(monthYear)
    #print(netchange)

    greatestincrease=-99999
    for i in range(len(netchange)):
        if netchange[i]>greatestincrease:
            greatestincrease=netchange[i]
            greatestincreasemonth=monthYear[i]
            #print(i)
            #print(monthYear[i])
        #print(netchange[i])

    greatestdecrease=999999999999
    for i in range(len(netchange)):
        if netchange[i]<greatestdecrease:
            greatestdecrease=netchange[i]
            greatestdecreasemonth=monthYear[i]
            #print(i)
            #print(monthYear[i])

        #print(netchange[i])
        
    print(greatestincrease)
    print(greatestincreasemonth)
    print(greatestdecrease)
    print(greatestdecreasemonth)

# Specify the file to write to
output_path=os.path.join("analysis", "budgetanalysis.txt")
output= (  
    f"Financial Analysis\n" +
    f"------------------------\n" +
    f"Total Months: {totalMonth}\n" +
    f"Total: ${totalNet}\n" +
    f"Average Change: ${averagechange}\n".format(round,2) +
    f"Greatest Increase in Profits: {greatestincrease} (${greatestincreasemonth})\n" +
    f"Greatest Decrease in Profits: {greatestdecrease} (${greatestdecreasemonth})\n")  
print(output)

# Open the file using "write" mode.  Specify the variable to hold the contents
with open(output, 'w', newline='') as text_file:
   text_file.write(output)

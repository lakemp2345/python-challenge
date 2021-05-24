import csv
import os
from typing import Text
output="/Users/laurakemp/Documents/Homework/python-challenge/PyBank/analysis/budgetanalysis.txt"

totalNet=0
totalMonth=0
netchange=[]
monthYear=[]
greatestdecreasemonth=""
greatestincreasemonth=''

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

    x=-99999
    for i in range(len(netchange)):
        if netchange[i]>x:
            x=netchange[i]
            greatestincreasemonth=monthYear[i]
            #print(i)
            #print(monthYear[i])
        #print(netchange[i])

    y=999999999999
    for i in range(len(netchange)):
        if netchange[i]<y:
            y=netchange[i]
            greatestdecreasemonth=monthYear[i]
            #print(i)
            #print(monthYear[i])

        #print(netchange[i])
        
    print(x)
    print(greatestincreasemonth)
    print(y)
    print(greatestdecreasemonth)

# Specify the file to write to
output_path=os.path.join("analysis", "budgetanalysis.txt")

# Open the file using "write" mode.  Specify the variable to hold the contents
with open(output, 'w', newline='') as text_file:
    output=str(budgetdata())
    text_to_write= ""
    text_to_write+=("Financial Analysis" ''
    text_to_write+= "Total Months: " ''
    text_to_write+=totalMonth ''
    text_to_write+="Total: " ''
    text_to_write+= "totalNet:${}".format ''
    text_to_write+="Average Change: "
    text_to_write+="averagechange:${}".format(round,2)
    text_to_write+= "Greatest Increase in Profits: "
    text_to_write+= greatestincreasemonth
    text_to_write+="x:${}".format 
    text_to_write+="Greatest Decrease in Profits:" 
    text_to_write+=greatestdecreasemonth 
    text_to_write+="y:${}".format 
    

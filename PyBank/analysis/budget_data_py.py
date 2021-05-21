# Open current budget CSV
with open(budget_data.csv, 'r') as csvFile:

csvReader=csv.reader(csvFile, delimiter=',')

# Skip headers
next(csvReader, None)

for row in csvReader:

    # Append data from the row
    date.append(row[0])
    profit/losses(row[1])

    # Calculate greatest increase and greatest decrease and append to the list
    greatestincrease.append

# Specify the file to write to
output_path=os.path.join("..", "output", "new.csv")

# Open the file using "write" mode.  Specify the variable to hold the contents
    with open(output_path, 'w', newline'') as csvfile:
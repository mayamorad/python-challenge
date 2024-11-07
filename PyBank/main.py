import csv
import os

# File paths
fileLoad = os.path.join("Resources", "budget_data.csv")  # Input file path
outputFile = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Initialize variables
totalMonths = 0 # initialize the total months to 0 
totalProfitLoss = 0  # initialize total profit/loss to 0
monthlyChanges = [] # initialize the list of monthly change
months = [] # initializes the list of months
greatestIncrease = ["", 0] # holds the month and the value of the greatest increase
greatestDecrease = ["", 0] # holds the month and the value of the greatest decrease

# Read the csv file
with open(fileLoad) as financialData:
    # create a csv reader object
    csvreader = csv.reader(financialData)

    # Skip the header row
    header = next(csvreader)
    # move to the first row 
    firstRow = next(csvreader)
    
    # increment the count of the total months
    totalMonths += 1 # same as totalMonths = totalMonths + 1
    
    # Add on to the total amount of revenue
    totalProfitLoss += float(firstRow[1])

    # establish the previous revenue
    previousRevenue = float(firstRow[1])
    
    # Process each row
    for row in csvreader:
       # increment the count of the total months
       totalMonths += 1
       
       # add to the total amount of revenue - revenue is in index 1
       totalProfitLoss += float(row[1])
       
       # Calculate monthly net change
       netChange = float(row[1]) - previousRevenue
       # add on to the list of monthly changes
       monthlyChanges.append(netChange)

       # add the first month that a change occurred
            # month is in index 0
       months.append(row[0])

       #update the previous revenue
       previousRevenue = float(row[1])

# Calculate the average monthly change
averageChangePerMonth = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]] # holds the month and the value of the greatest increase
greatestDecrease = [months[0], monthlyChanges[0]] # holds the month and the value of the greatest decreasefor m in monthlyChanges:

# use loop to calculate the index of the greatest and least monthly change
for m in range(len(monthlyChanges)): 
    # calculate the greatest increase and decrease
    if(monthlyChanges[m] > greatestIncrease[1]): 
        # if the value is greater than the greatest increase, that value becomes the new greatest increase
        greatestIncrease[1] = monthlyChanges[m]
        # update the month
        greatestIncrease[0] = months[m]

    if(monthlyChanges[m] < greatestDecrease[1]): 
        # if the value is less than the greatest decrease, that value becomes the new greatest decrease
        greatestDecrease[1] = monthlyChanges[m]
        # update the month
        greatestDecrease[0] = months[m]

# Generate output summary
output = (
    f"\nFinancial Analysis \n"
    f"--------------------------- \n"
    f"\n"
    f"Total Months : {totalMonths} \n"
    f"Total : ${totalProfitLoss:,.2f} \n"
    f"Average Change : ${averageChangePerMonth:,.2f} \n"
    f"Greatest Increase in Profits : {greatestIncrease[0]} ( ${greatestIncrease[1]:,.2f} ) \n"
    f"Greatest Decrease in Profits : {greatestDecrease[0]} ( ${greatestDecrease[1]:,.2f} ) \n"
    )

# Print output to the console/terminal
print(output)

# Write output to text file
with open(outputFile, "w") as textFile:
    textFile.write(output)
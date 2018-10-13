import os
import csv

# Initiate variables
csvDate, csvProfit, changeInProfit = [], [], []
rowCount, i = 0, 0
# Path to collect data from the Resources folder
budgetCSV = os.path.join('.', 'Resources', 'budget_data.csv')

# First define function to store lists
def getDateProfitLists(rowData):
  # Append date and Profit to List
  csvDate.append(rowData[0])
  csvProfit.append(int(rowData[1]))

# Read in the CSV file
with open(budgetCSV, 'r', encoding='utf-8', newline='') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # File has header as first row
    header = next(csvreader)
    # Loop through the data
    for row in csvreader:
      # increment row counter
      rowCount += 1
      # call function getResults
      getDateProfitLists(row)

for i in range(1, len(csvProfit)):
  change = csvProfit[i] - csvProfit[i-1]
  changeInProfit.append(change)

# First looking at List csvProfit
# add values in List csvProfit
total = sum(csvProfit)
# average of values in List csvProfit
avg = int(total / len(csvProfit))
# highest profit, its index/position value, corresponding date
hp = max(csvProfit)
hpi = csvProfit.index(max(csvProfit))
hpd = csvDate[hpi]
# highest loss, its index/position value, corresponding date
hl = min(csvProfit)
hli = csvProfit.index(min(csvProfit))
hld = csvDate[hli]

# Second looking at List changeInProfit
# add values in List changeInProfit
totalChange = sum(changeInProfit)
# average of values in List changeInProfit
avgChange = int(totalChange / len(changeInProfit))
# highest positive change in profit, index and date
hPosCh = max(changeInProfit)
hPosChi = changeInProfit.index(max(changeInProfit))
hPosChd = csvDate[hPosChi + 1]
# highest negative change in profit, index and date
hNegCh = min(changeInProfit)
hNegChi = changeInProfit.index(min(changeInProfit))
hNegChd = csvDate[hNegChi + 1]

# Specify the file to write to
output_path = os.path.join(".", "output", "results.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', encoding='utf-8') as resultsFile:
    # Write the 1st row
    resultsFile.write("----------Main Stats------------\n")
    # Write the 2nd row
    resultsFile.write(f"Total Months: {rowCount}\n")
    # Write the 3rd row
    resultsFile.write(f"Total Profits: ${total}\n")
    # Write the 4th row
    resultsFile.write(f"Average change in Profits: ${avgChange}\n")
    # Write the 5th row
    resultsFile.write(
        f"Greatest increase in Profits: ${hPosCh} in the month of {hPosChd}\n")
    # Write the 6th row
    resultsFile.write(
        f"Greatest decrease in Profits: ${hNegCh} in the month of {hNegChd}\n")

# Print results to Terminal
print("\r")
print("----------Main Stats------------")
print(f"Total Months: {rowCount}")
print(f"Total Profits: ${total}")
print(f"Average change in Profits: ${avgChange}")
print(f"Greatest increase in Profits: ${hPosCh} in the month of {hPosChd}")
print(f"Greatest decrease in Profits: ${hNegCh} in the month of {hNegChd}")

print("\n")
print("----------Other Stats------------")
print(f"Average Profit: ${avg}")
print(f"Highest Profit: ${hp}")
print(f"Highest Profit Month#: {hpi}")
print(f"Highest Profit Date: {hpd}")
print(f"Highest Loss: {hl}")
print(f"Highest Loss Month#: {hli}")
print(f"Highest Loss Date: {hld}")

print("\n")
print("----------Data Lists----------------")
print(f"Dates List: {csvDate}\n")
print(f"Profit List: {csvProfit}\n")
print(f"Change in Profit List: {changeInProfit}")

import os
import csv

# Initializing variables
counters = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}

# Path to collect data from the Resources folder
pollingCSV = os.path.join('.', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(pollingCSV, 'r', encoding='utf-8', newline='') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # File has header as first row
    header = next(csvreader)
    # Loop through the data
    for row in csvreader:
      if (row[2] == "Khan"):
        counters["Khan"] += 1
      elif (row[2] == "Correy"):
        counters["Correy"] += 1
      elif (row[2] == "Li"):
        counters["Li"] += 1
      elif (row[2] == "O'Tooley"):
        counters["O'Tooley"] += 1

totalVotes = counters["Khan"] + counters["Correy"] + \
    counters["Li"] + counters["O'Tooley"]

khanPercent = str(round((counters["Khan"] / totalVotes * 100), 3))
correyPercent = str(round((counters["Correy"] / totalVotes * 100), 3))
liPercent = str(round((counters["Li"] / totalVotes * 100), 3))
tooleyPercent = str(round((counters["O'Tooley"] / totalVotes * 100), 3))

# use lambda to loop through values of keys within dictionary 
# and return key with highest value
winner = max(counters, key=lambda k: counters[k])

# Specify the file to write to
output_path = os.path.join(".", "output", "results.txt")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', encoding='utf-8') as resultsFile:
    resultsFile.write("----------Election Results---------\n")
    resultsFile.write("-----------------------------------\n")
    resultsFile.write(f"Total Votes: {totalVotes}\n")
    resultsFile.write("-----------------------------------\n")
    resultsFile.write(f'Khan votes: {khanPercent}% ({counters["Khan"]})\n')
    resultsFile.write(f'Correy votes: {correyPercent}% ({counters["Correy"]})\n')
    resultsFile.write(f'Li votes: {liPercent}% ({counters["Li"]})\n')
    resultsFile.write("O'Tooley votes: " + str(tooleyPercent) +
                      "% (" + str(counters["O'Tooley"]) + ")\n")
    resultsFile.write("-----------------------------------\n")
    resultsFile.write(f"Winner is {winner}\n")
    resultsFile.write("-----------------------------------\n")

# Print results to Terminal
print("\r")
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {totalVotes}")
print("-----------------------------------")
print(f'Khan votes: {khanPercent}% ({counters["Khan"]})')
print(f'Correy votes: {correyPercent}% ({counters["Correy"]})')
print(f'Li votes: {liPercent}% ({counters["Li"]})')
print("O'Tooley votes: " + str(tooleyPercent) +
      "% (" + str(counters["O'Tooley"]) + ")")
print("-----------------------------------")
print(f"Winner is {winner}")
print("-----------------------------------")

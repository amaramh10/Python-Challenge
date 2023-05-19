#Import dependencies

import os
import csv
from pathlib import Path

#Join the path to collect the data from
budget_csv = Path("/Users/amaramh/Desktop/Analysis Projects/Python-Challenge/PyBank/Resources/budget_data_copy.csv")

# Variables & Lists to store data
totalmonths = 0 
monthschange = []
totalnet = 0
netchangelist = []
currentmonthloss = 0
previousmonthloss = 0
netchanges = 0


# Open & Read CSV file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    #print(header)

    #Read through each row
    for row in csvreader:

        #Count the total months included in the data set
        totalmonths += 1

        #Total amount of profit/losses
        currentmonthloss = int(row[1])
        totalnet += currentmonthloss

        #Value of previous month = to current month
        if totalmonths == 1: 
            previousmonthloss = currentmonthloss

        else:

            #Add total amount of months
            monthschange.append(row[0])

            #Calculate the change in net change loss
            netchanges = currentmonthloss - previousmonthloss

            #Add each net change loss into the netchangelist
            netchangelist.append(netchanges)

            #Reset previous month to be = to current month
            previousmonthloss = currentmonthloss

#Calculate the sum & average of profit/losses            
totalprofitloss = sum([netchanges])
entireperiod = totalmonths - 1
averageprofitloss = round(totalprofitloss/entireperiod, 2)

#Calculate the min & max of profit/losses
maxchange = max(netchangelist)
minchange = min(netchangelist)
# print(minchange)
# print(maxchange)

#List the point of the highest & lowest values of profit/losses
highestpoint = netchangelist.index(maxchange)
lowestpoint = netchangelist.index(minchange)

#Show the best & worst months
bestmonth = monthschange[highestpoint]
worstmonth = monthschange[lowestpoint]

#Print Analysis to Terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {totalmonths}")
print(f"Total:  ${totalnet}")
print(f"Average Change:  ${averageprofitloss}")
print(f"Greatest Increase in Profits:  {bestmonth} (${maxchange})")
print(f"Greatest Decrease in Losses:  {worstmonth} (${minchange})")

#
budgetdatafile = ("budget_analysis.txt")
with open(budgetdatafile, "w") as output:

    output.write("Financial Analysis")
    output.write("----------------------------")
    output.write(f"Total Months:  {totalmonths}")
    output.write(f"Total:  ${totalnet}")
    output.write(f"Average Change:  ${averageprofitloss}")
    output.write(f"Greatest Increase in Profits:  {bestmonth} (${maxchange})")
    output.write(f"Greatest Decrease in Losses:  {worstmonth} (${minchange})")


               



    


#Set variable for output path
#  output = ("Analysis/budget_analysis.txt")
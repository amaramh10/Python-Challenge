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

#Calculate the min & max of profit losses
maxchange = max([netchanges])
minchange = min([netchanges])


            



               



    


#Set variable for output path
#  output = ("Analysis/budget_analysis.txt")
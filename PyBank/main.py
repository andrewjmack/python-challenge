#import modules for cross-OS functionality and CSV file reading
import os
import csv

#CSV file path
csvpath = os.path.join("Resources", "budget_data.csv")

#read in CSV
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    #store header
    csv_header = next(csvreader)

    #empty lists to store loop values
    months = []
    profits_losses = []
 
    #read each row of data after the header:
    for row in csvreader:

        #add to months list with each loop iteration
        months.append(row[0])

        #add to profits_losses list with each loop iteration
        profits_losses.append(int(row[1]))

    #print analysis header
    print(f"Financial Analysis \n",
        f"----------------------------",)

    #count the number of month elements captured in the months list
    months_total = len(months)
    print(f"Total Months: {months_total}")
    
    #sum the profits and losses for the entire period
    total_profit_loss = sum(profits_losses)
    print(f"Net total: ${total_profit_loss}")

    #loop and store profits_losses current month minus prior month
    monthly_PL_changes = []
    for i in range(1, len(profits_losses)):
        x = profits_losses[i] - profits_losses[i-1]
        monthly_PL_changes.append(x)

    #Average of the changes in "Profit/Losses" over the entire period
    avg_change_PL = round(sum(monthly_PL_changes)/len(monthly_PL_changes),2)
    print(f"Average Change: ${avg_change_PL}")

    #The greatest increase in profits (date and amount) over the entire period
    max_change = max(monthly_PL_changes)
    max_i = monthly_PL_changes.index(max_change) + 1
    max_month = months[max_i]
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    
    #The greatest decrease in profits (date and amount) over the entire period
    min_change = min(monthly_PL_changes)
    min_i = monthly_PL_changes.index(min_change) + 1
    min_month = months[min_i]
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

    #The open() and writelines() functions create a text file and write the results to separate lines
    #BEWARE that this code block WILL overwrite an existing file of the same name and location!
    file = open("analysis/PyBankAnalysis.txt", "w")
    results = [f"Financial Analysis \n",
                f"---------------------------- \n",
                f"Total Months: {months_total} \n",
                f"Net total: ${total_profit_loss} \n",
                f"Average Change: ${avg_change_PL} \n",
                f"Greatest Increase in Profits: {max_month} (${max_change}) \n",
                f"Greatest Decrease in Profits: {min_month} (${min_change})"
    ]
    file.writelines(results)
    file.close()
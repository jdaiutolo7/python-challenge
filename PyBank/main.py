import os
import csv

budget_data = os.path.join(".\\PyBank\Resources/budget_data.csv")

# Lists to store data
months = []
profit = []
change_in_profit = []

# Open csv file, assign it to a variable, and then skip the header values
with open(budget_data, encoding="utf-8") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",") 
    csvheader = next(csvreader)  

    # Creating a for loop to append the total months and profit
    for row in csvreader: 

        months.append(row[0])
        profit.append(int(row[1]))

    # Creating a for loop to append the change in profit
    for i in range(len(profit)-1):
        
        change_in_profit.append(profit[i+1]-profit[i])
        
# Obtaining the maximum and minimum (increase/decrease) value of the monthly change in profit
max_increase_value = max(change_in_profit)
max_decrease_value = min(change_in_profit)

# Assigning maximum and minimum to the correct month
max_increase_month = change_in_profit.index(max(change_in_profit)) + 1
max_decrease_month = change_in_profit.index(min(change_in_profit)) + 1 

# Print
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_in_profit)/len(change_in_profit),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")

# Assigning variable for text file and opening it
PyBank_Analysis = os.path.join(".\\PyBank\Analysis/pybank_analysis.txt")

with open(PyBank_Analysis,"w") as txtfile:  
# Write on a txt file
    txtfile.write("Financial Analysis \n")
    txtfile.write("---------------------------- \n")
    txtfile.write(f"Total Months: {len(months)} \n")
    txtfile.write(f"Total: ${sum(profit)} \n")
    txtfile.write(f"Average Change: {round(sum(change_in_profit)/len(change_in_profit),2)} \n")
    txtfile.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))}) \n")
    txtfile.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(max_decrease_value))})")
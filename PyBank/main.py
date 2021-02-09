import csv

total_months = 0
total_profit_loss = 0.00
#average_profit_loss = 0.00
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}
temp = 0.00
change_profit = 0.00
change_profit_list = []

file_path = "./Resources/Budget_data.csv"
output_file = "./Analysis/output.txt"

with open(file_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    # Read the header row first(skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        # The total number of months included in the dataset
        total_months = total_months + 1
        date = row[0]
        profit = float(row[1])

        # The net total amount of "Profit/Losses" over the entire period
        total_profit_loss = total_profit_loss + profit

        # calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
        if row[0] != "Jan-2010":
            change_profit = profit - temp
            change_profit_list.append(change_profit)
        temp = profit

        # The greatest increase in profits(date and amount) over the entire period
        if (profit > greatest_increase["amount"]):
            greatest_increase["date"] = date
            greatest_increase["amount"] = profit
            # The greatest decrease in losses(date and amount) over the entire period
        if (profit < greatest_decrease["amount"]):
            greatest_decrease["date"] = date
            greatest_decrease["amount"] = profit

# print results
print("Finacial Analysis")
print("----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_profit_loss}")
print(f"Average:{round(sum(change_profit_list) / (total_months - 1), 2)}")
print(
    f"Greatest Increase in Profits:{greatest_increase['date']} (${greatest_increase['amount']})")
print(
    f"Greatest Decrease in Profits:{greatest_decrease['date']} (${greatest_decrease['amount']})")

# Write to a file
with open(output_file, 'w') as outputFile:
    outputFile.write("Finacial Analysis")
    outputFile.write("----------------------------------\n")
    outputFile.write(f"Total Months: {total_months}\n")
    outputFile.write(f"Total: {total_profit_loss}\n")
    outputFile.write(
        f"Average:{round(sum(change_profit_list) / (total_months - 1), 2)}\n")
    outputFile.write(
        f"Greatest Increase in Profits:{greatest_increase['date']} (${greatest_increase['amount']})\n")
    outputFile.write(
        f"Greatest Decrease in Profits:{greatest_decrease['date']} (${greatest_decrease['amount']})\n")

# # Results shoud look like this
# # Financial Analysis
# # ----------------------------
# # Total Months: 86
# # Total: $38382578
# # Average  Change: $-2315.12
# # Greatest Increase in Profits: Feb-2012 ($1926159)
# # Greatest Decrease in Profits: Sep-2013 ($-2196167)

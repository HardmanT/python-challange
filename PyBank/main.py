import os
import csv

# Creating path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

months = 0
total_profit_losses = 0
previous_profit_loss = 0
changes_in_profit_losses = []
dates = []

# Read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:
        # Extracting data from the current row
        date = row[0]
        profit_loss = int(row[1])

        # Calculateing total months and total profit/loss
        months += 1
        total_profit_losses += profit_loss

        # Calculateing changes in profit/loss
        if months > 1:
            change = profit_loss - previous_profit_loss
            changes_in_profit_losses.append(change)
            dates.append(date)

        previous_profit_loss = profit_loss

# Calculateing average change
average_change = sum(changes_in_profit_losses) / len(changes_in_profit_losses)

# Finding the greatest increase and decrease in profits
greatest_increase = max(changes_in_profit_losses)
greatest_increase_index = changes_in_profit_losses.index(greatest_increase)
greatest_increase_date = dates[greatest_increase_index]

greatest_decrease = min(changes_in_profit_losses)
greatest_decrease_index = changes_in_profit_losses.index(greatest_decrease)
greatest_decrease_date = dates[greatest_decrease_index]

# Printing the results and written to text file
print("Financial Analysis")
print('')
print("----------------------------")
print('')
print(f"Total Months: {months}")
print('')
print(f"Total: ${total_profit_losses}")
print('')
print(f"Average Change: ${average_change:.2f}")
print('')
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print('')
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_file_path = 'analysis/Financial_Analysis.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {months}\n")
    output_file.write(f"Total: ${total_profit_losses}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
print('')
print(f"Statement has been written to {output_file_path}")
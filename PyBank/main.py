import csv


total_months=0
net_total=0
previous_profit_loss=0
profit_loss_changes = []
dates = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

csv_file_path = "C:/Users/darvarir/Documents/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv"
with open(csv_file_path, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    for row in csvreader:
        
        date = row[0]
        profit_loss = int(row[1])
        
         # Calculate the total number of months
        total_months += 1
        
        # Calculate the net total amount of profit/losses
        net_total += profit_loss
        
        #Calculate the change over time
        change=profit_loss-previous_profit_loss
        profit_loss_changes.append(change)
        dates.append(date)
        
         # Determine the greatest increase and decrease in profits
        if change>greatest_increase["amount"]:
            greatest_increase["date"]=date
            greatest_increase["amount"]=change
            
        if change<greatest_decrease["amount"]:
            greatest_decrease["date"]=date
            greatest_decrease["amount"]=change
            
            
        previous_profit_loss=profit_loss
        
        
# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes[1:]) / (total_months - 1)
average_change = round(average_change, 2)  # Convert to float and round
average_change = "${:,.2f}".format(average_change)  # Format as a string


# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
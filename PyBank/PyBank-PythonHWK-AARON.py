import os
import csv
path = os.path.join("Resources", "budget_data.csv")
with open(path, 'r', newline='') as bdata:
    csvreader = csv.reader(bdata, delimiter=',')
    csv_head = next(csvreader)
    months = []
    net_change = []
    for each in csvreader:
        months.append(each[0])
        net_change.append(int(each[1]))
    month_num = len(net_change)
    net_total = sum(net_change)
    change = [int(j-i) for i, j in zip(net_change[:-1], net_change[1:])]
    avg_change = round((sum(change)/len(change)),2)
    max_inc = max(change)
    max_dec = min(change)
    max_inc_month = months[(change.index(max_inc) + 1)]
    max_dec_month = months[(change.index(max_dec) + 1)]
    # Final Analysis
    print("Financial Analysis\n---------------------------------------------------")
    print("Total Months: %s" % month_num)
    print("Total: %s" % net_total)
    print("Average  Change: $%s" % avg_change)
    print("Greatest Increase in Profits: %s ($%s)" % (max_inc_month, max_inc))
    print("Greatest Decrease in Profits: %s ($%s)" % (max_dec_month, max_dec))
    with open("financial_analysis.txt", 'w') as text:
        text.write("Financial Analysis\n---------------------------------------------------\n")
        text.write("Total Months: %s\n" % month_num)
        text.write("Average  Change: $%s\n" % avg_change)
        text.write("Greatest Increase in Profits: %s ($%s)\n" % (max_inc_month, max_inc))
        text.write("Greatest Decrease in Profits: %s ($%s)\n" % (max_dec_month, max_dec))
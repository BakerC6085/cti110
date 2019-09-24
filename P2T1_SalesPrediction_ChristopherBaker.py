# A Sales Predicition program
# 9/24/19
# CTI-110 P2T1 - Sales Prediction
# Christopher Baker
#

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit.
print('The profit is $', format(profit, ',.2f'))

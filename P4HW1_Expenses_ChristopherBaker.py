# CTI-110
# P4HW1 - Expenses
# Christopher Baker
# 10-17-19

# Input amount already inside the account
Account = int(input('Enter starting amount in accout?' ))

# Create a variable to control the loop
more = 'y'

# Create a variable to control number of expenses
number = 0

# Calculate the expenses
while more == 'y':
    
    # Get the Expense for user
    Expense = float(input('Enter expense:'))

    # Get number of expenses added
    Num_Expenses = int(number) + 1

    # Calculate the balance
    Balance = Account - Expense

    # Ask user if they have another expense
    more = input('Do you want to enter another expense? (y/n): ')

# Give the account balance before expense
print('Amount in account before expense subtraction: $', format(Account, ',.2f'))
print('Number of expeses entered: ', Num_Expenses)

# Give the user their new account balance
print('Amount in account AFTER expenses subtracted is $', format(Balance, ',.2f'))

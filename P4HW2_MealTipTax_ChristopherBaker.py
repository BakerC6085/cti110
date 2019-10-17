# CTI-110
# P3HW2 - MealTipTax
# Christopher Baker
# 10/3/2019
#

# Creating a constant for loop
keep_going = 'y'
    
# Ask user to input meal cost.
Meal = int(input('Please enter meal cost: '))

# Constant is the sales tax.
Tax16 = Meal * 0.06
Tax18 = Meal * 0.06
Tax20 = Meal * 0.06
Tip16 = 0.16 * Meal
Tip18 = 0.18 * Meal
Tip20 = 0.2 * Meal

# Calculate the tip.
Cost16 = Meal + Tip16 + Tax16
Cost18 = Meal + Tip18 + Tax18
Cost20 = Meal + Tip20 + Tax20



# Making a loop
while keep_going == 'y':
    
    # Ask user to input tip percentage.
    Tip = int(input('Please enter tip percenatage, 16, 18, or 20: '))

    # Code for Validation of tip input
    while Tip < 16 or Tip > 18:
        print('ERROR: Tip only valid with 16, 18, or 20')
        Tip = int(input('Please enter tip percentage, 16, 18, or 20: '))
    
    # Display the meal total.
    if Tip == 16:
        print('The total cost of the meal is', format(Cost16, ',.2f'))
    elif Tip == 18:
        print('The total cost of the meal is', format(Cost18, ',.2f'))
    elif Tip == 20:
        print('The total cost of the meal is', format(Cost20, ',.2f'))
    # See if user wishes to keep going
    keep_going = input('Do you wish to enter another tip? y/n: ')
    

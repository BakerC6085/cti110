# A program to calculate the tip for the meal.
# 9/24/19
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Christopher Baker
#

# Cost of the meal
meal_cost = float(input('Enter the meal cost: '))

# Enter the Tip Amount
tip = float(input('Enter the tip amount: '))

# Enter the Tax Amount
tax = float(input('Enter the tax Amount: '))

# Calculate the tip amount.
Calculated_tip = meal_cost * tip

# Calculcate the tax amount.
Calculated_tax = meal_cost * tax

# Calculate the total meal cost.
meal_total = meal_cost + Calculated_tip + Calculated_tax

# Display the Calculated tip
print('The Calculated Tip is $', format(Calculated_tip, ',.2f'))

# Display the Calculated tax.
print('The Calculated tax is $', format(Calculated_tax, ',.2f'))

# Display the total meal cost.
print('The total meal cost is $', format(meal_total, ',.2f'))

# CTI-110
# P3HW2 - MealTipTax
# Christopher Baker
# 10/3/2019
#
# Ask user to input meal cost.
Meal = int(input('Please enter meal cost: '))

# Ask user to input tip percentage.
Tip = int(input('Please enter tip percenatage, 16, 18, or 20: '))

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

# Display the meal total.
if Tip == 16:
    print('The total cost of the meal is', Cost16)
elif Tip == 18:
    print('The total cost of the meal is', Cost18)
elif Tip == 20:
    print('The total cost of the meal is', Cost20)
else:
    print('Error please enter 16, 18, or 20')


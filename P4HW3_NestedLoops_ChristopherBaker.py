# Creating the figure given using nested loops
# 10-17-19
# CTI-110 P4HW3 - Nested Loops
# Christopher Baker
#
# Making the first loop
for row in range(6):
    print('#', end='', sep='')
    # Making the nested loop to create the spaces between the #
    for spaces in range(row):
        print( ' ', end='', sep='')
    # Making the second #
    print('#', sep='')

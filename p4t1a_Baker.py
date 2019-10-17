# Creating squares using nested loops
# 10-17-19
# CTI-110 P4T1a
# Christopher Baker

# Imports Turtle
from turtle import Turtle, Screen

# Named Constants
DELTA = 3
MINIMUM = DELTA * 2
CURSOR_SIZE = 20

num_squares = -1

# Gets input for user on the number of squares needed. In this case 100
while num_squares < 1:
    try:
        num_squares = int(input('Input the number of squares: '))
    except ValueError:
        print("please enter an integer.")

    if num_squares < 1:
        print("You must have at least 1 square.")

# Starts Turtle 
screen = Screen()
turtle = Turtle("square", visible=False)
turtle.fillcolor("white")

# Uses a loop to stamp the squares into place instead of drawing them.
for size in range(((num_squares - 1) * DELTA) + MINIMUM, MINIMUM - 1, -DELTA):
    turtle.goto(turtle.xcor() + DELTA/2, turtle.ycor() - DELTA/2)
    turtle.shapesize(size / CURSOR_SIZE)
    turtle.stamp()

# Closes turtle when the user clicks.
screen.exitonclick()

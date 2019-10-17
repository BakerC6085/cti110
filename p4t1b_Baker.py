# Creating my Initals with Turtle
# CTI-110
# 10-17-19
# Christopher Baker

# Import Turtle and changing turtle
import turtle
chris = turtle.Turtle()
turtle.Screen().bgcolor("black")
chris.color("red")

# Drawing my initals
chris.lt(180)
chris.fd(30)
chris.rt(90)
chris.fd(50)
chris.rt(90)
chris.fd(30)

chris.pu()

chris.fd(30)

chris.pd()

chris.fd(30)
chris.rt(90)
chris.fd(50)
chris.rt(90)
chris.fd(30)
chris.rt(90)
chris.fd(25)
chris.rt(90)
chris.fd(30)
chris.bk(30)
chris.lt(90)
chris.fd(25)

# make it so that you exit turtle on on a click.
turtle.exitonclick()

from turtle import *
import math
# Name your Turtle.
Rocky = Turtle()

# Set Up your screen and starting position.
Rocky.penup()
setup(500,300)
x_pos = -250
y_pos = -150
Rocky.setposition(x_pos, y_pos)

### Write your code below:
#answer= input="What color would you like your square to be?"

def square(steps, angle, s):
    Rocky.pendown()
    Rocky.speed(s)
    Rocky.forward(steps)
    Rocky.right(angle)
    Rocky.forward(steps)
    Rocky.right(angle)
    Rocky.forward(steps)
    Rocky.right(angle)
    Rocky.forward(steps)
    Rocky.right(angle)
    print("This is a square!")

square(100, 20, 20)

int("5")

answer = input("question")
int(answer)

# Close window on click.
exitonclick()

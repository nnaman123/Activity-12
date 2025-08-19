#spiral pattern with cross and text

import turtle
import time

my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.setup(600, 600)
my_wn.title("Turtle")
my_pen = turtle.Turtle()
my_pen.speed(1)

size = 0
start_time = time.time()

# Draw spiral for 30 seconds
while time.time() - start_time < 30:
    for i in range(4):
        my_pen.fd(size + 1)
        my_pen.left(90)
        size = size - 5
    size = size + 1

# Draw a cross at the center
my_pen.penup()
my_pen.goto(0, 0)
my_pen.pendown()
my_pen.pencolor("red")
my_pen.pensize(5)

# Vertical line
my_pen.setheading(90)
my_pen.forward(200)
my_pen.backward(400)
my_pen.forward(200)

# Horizontal line
my_pen.setheading(0)
my_pen.forward(200)
my_pen.backward(400)
my_pen.forward(200)

# Write "IDK" quickly on top
my_pen.penup()
my_pen.goto(0, 220)
my_pen.pencolor("black")
my_pen.pensize(1)
my_pen.write("ILC\n I Love Codingal", align="center", font=("Arial", 48, "bold"))

turtle.done()
#star
import turtle

turtle.Screen().bgcolor("aqua")
board = turtle.Turtle()
board.speed(1)

#first triangle for a star
board.forward(100)

board.left(120)
board.forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

#second triangle for a star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()  # to finish the drawing and keep the window open
# This code draws a star using two triangles with the turtle graphics library.

import turtle #importing the turtle module
turtle.Screen().bgcolor("black") #setting the background color to black
turtle.Screen().setup(300, 400) #setting the screen size
polygon = turtle.Turtle() #creating a turtle object
polygon.pencolor("white") # set pen color to white
polygon.speed(1) #setting the speed of the turtle to maximum

num_sides = 10 #number of sides for the polygon
side_length = 70 #length of each side
angle = 360 / num_sides #calculating the angle for the polygon
#iterate loop to draw the polygon
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done() #to finish the drawing and keep the window open
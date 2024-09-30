import time
import turtle
from turtle import Turtle, Screen

turtle.tracer(0)
#  Create Objects
tom_head = Turtle()
window = Screen()

#  Set window background
window.bgcolor("black")

#
snake_body = []
#  Snake movements
def moveRight():
    tom_head.right(90)
def moveLeft():
    tom_head.left(-90)

#  Snake head
tom_head.penup()
tom_head.shape("circle")
tom_head.shapesize(1.5, 1.5, 1)
tom_head.color("white")
#  Store on array
snake_body.append(tom_head)


#  Create Snake Body
x_axis = -21
y_axit = 0
for body in range(3):
    tom_body = Turtle()
    tom_body.penup()
    tom_body.shape("square")
    tom_body.color("white")
    tom_body.goto(x_axis, y_axit)
    x_axis += -21
    snake_body.append(tom_body)
#
window.listen()
window.onkeypress(moveRight, "Right")
window.onkeypress(moveLeft, "Left")

#  Movies
while True:
    turtle.update()
    time.sleep(0.1)
    for bodies in snake_body:
        bodies.speed(1)
        bodies.forward(15)



#  tracer off
turtle.update()


# Exit
window.exitonclick()

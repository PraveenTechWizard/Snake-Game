from turtle import Turtle, Screen

#  Create Objects
tom = Turtle()
window = Screen()

#  Set window background
window.bgcolor("black")

#  Snake movements
def snakeMovement(snake_head):
    pass

#  Snake head
tom.penup()
tom.shape("circle")
tom.shapesize(1.5, 1.5, 1)
tom.color("white")

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


# Exit
window.exitonclick()

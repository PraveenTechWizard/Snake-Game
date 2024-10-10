from turtle import Turtle
#
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
    #
    def create_snake(self):
        self.snakeHead()
        self.snakeBody()
    #
    def snakeHead(self):
        self.tom_head = Turtle()
        #  Snake head
        self.tom_head.penup()
        self.tom_head.shape("circle")
        self.tom_head.shapesize(1.5, 1.5, 1)
        self.tom_head.color("white")
        self.tom_head.goto(0, 0)
        #  Store on array
        self.snake_body.append(self.tom_head)
    #
    def snakeBody(self):
        x_axis = -20
        for _ in range(5):
            self.tom_body = Turtle()
            self.tom_body.penup()
            self.tom_body.shape("square")
            self.tom_body.color("white")
            self.tom_body.goto(x_axis, 0)
            x_axis -= 20
            self.snake_body.append(self.tom_body)

    #
    def moves(self):
        for path in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[path - 1].xcor()
            new_y = self.snake_body[path - 1].ycor()
            #
            self.snake_body[path].goto(new_x, new_y)
            print(f"x:{new_x} y:{new_y}")
            #
        self.tom_head.speed(1)
        self.tom_head.forward(10)

    #     Snake Movements
    def up(self):
        if self.tom_head.heading() != DOWN:
            self.tom_head.setheading(UP)

    def down(self):
        if self.tom_head.heading() != UP:
            self.tom_head.setheading(270)

    def left(self):
        if self.tom_head.heading() != RIGHT:
            self.tom_head.setheading(180)

    def right(self):
        if self.tom_head.heading() != LEFT:
            self.tom_head.setheading(0)

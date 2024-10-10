import time
from turtle import Turtle, Screen
from snake import Snake

#  Create Objects
window = Screen()
window.tracer(0)
window.listen()
#  Set window background
window.bgcolor("black")

#  Create snake object
snake = Snake()

#  Moviesment call
window.onkey(snake.up, "Up")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")
window.onkey(snake.down, "Down")

#  Movies
while True:
    window.update()
    time.sleep(0.1)
    #
    snake.moves()


# Exit
window.exitonclick()

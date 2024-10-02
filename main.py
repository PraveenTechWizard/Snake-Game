import time
from turtle import Turtle, Screen
from snake import Snake

#  Create Objects
window = Screen()
window.tracer(0)
#  Set window background
window.bgcolor("black")

#  Create snake object
snake = Snake()

#  Movies
while True:
    window.update()
    time.sleep(0.1)
    #
    snake.moves()


# Exit
window.exitonclick()

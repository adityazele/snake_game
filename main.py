# TODO 1: Create a snake body
# TODO 2: Move the snake
# TODO 3: Control the snake
# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail

from turtle import Screen
from snake import Snake
import time

game_is_on = True

screen = Screen()
screen.tracer(0)
screen.title('snake game')
screen.bgcolor('black')

slither = Snake()

screen.listen()
screen.onkey(slither.up, 'Up')
screen.onkey(slither.down, 'Down')
screen.onkey(slither.right, 'Right')
screen.onkey(slither.left, 'Left')

while game_is_on:
    screen.update()
    slither.move()
    time.sleep(0.1)

screen.exitonclick()

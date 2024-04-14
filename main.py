# 1: Create a snake body
# 2: Move the snake
# 3: Control the snake
# 4: Detect collision with food
# 5: Create a scoreboard
# 6: Detect collision with wall
# 7: Detect collision with tail

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

game_is_on = True

screen = Screen()
screen.setup(width=1000, height=600)
screen.tracer(0)
screen.title('snake game')
screen.bgcolor('black')

slither = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(slither.up, 'Up')
screen.onkey(slither.down, 'Down')
screen.onkey(slither.right, 'Right')
screen.onkey(slither.left, 'Left')

while game_is_on:
    screen.update()
    if -20 < food.x - slither.head.xcor() < 20 and -20 < food.y - slither.head.ycor() < 20:
        print('collision detected')
        food.food.hideturtle()
        food.generate_food()
        slither.increase_length()
        scoreboard.update_score()
    slither.move()
    if slither.head.xcor() >= 490 or slither.head.xcor() <= -490 or slither.head.ycor() >= 290 or slither.head.ycor() <= -290:
        game_is_on = False
    for seg in slither.snake_segments[2:]:
        if -20 < seg.xcor()-slither.head.xcor() < 20 and -20 < seg.ycor()-slither.head.ycor() < 20:
            print('tail collision')
            game_is_on = False
    time.sleep(0.1)

screen.exitonclick()

from turtle import Turtle, Screen
import time


class Snake:

    def __init__(self):
        self.screen = Screen()
        self.screen.listen()
        self.screen.title("Snake Game")
        self.screen.bgcolor('black')
        self.game_is_on = True
        self.x = 0
        self.y = 0
        self.snake_body = []
        for _ in range(3):
            self.snake_unit = Turtle("square")
            self.snake_unit.penup()
            self.snake_unit.color("white")
            self.snake_unit.goto(self.x, self.y)
            self.x -= 20
            self.snake_body.append(self.snake_unit)
        self.move()
        self.screen.exitonclick()

    def move(self):
        while self.game_is_on:
            time.sleep(0.1)
            self.screen.onkey(self.up, "Up")
            self.screen.onkey(self.down, "Down")
            self.screen.onkey(self.right, "Right")
            self.screen.onkey(self.left, "Left")
            length = len(self.snake_body)
            for i in range(length):
                if i != length-1:
                    self.snake_body[length-i-1].goto(self.snake_body[length-i-2].position())
                else:
                    self.snake_body[length - i - 1].forward(20)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

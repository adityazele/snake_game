from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = None
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for _ in range(3):
            self.snake = Turtle()
            self.snake.shape('square')
            self.snake.color('white')
            self.snake.penup()
            self.snake.goto(x, y)
            x -= 20
            self.snake_segments.append(self.snake)

    def increase_length(self):
        self.snake = Turtle()
        self.snake.shape('square')
        self.snake.color('white')
        self.snake.penup()
        x = self.snake_segments[-1].xcor() - 20
        y = self.snake_segments[-1].ycor()
        self.snake.goto(x, y)
        self.snake_segments.append(self.snake)

    def move(self):
        for seg in reversed(range(len(self.snake_segments))):
            if seg != 0:
                new_seg = seg - 1
                x_cor = self.snake_segments[new_seg].xcor()
                y_cor = self.snake_segments[new_seg].ycor()
                self.snake_segments[seg].goto(x_cor, y_cor)
            else:
                self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

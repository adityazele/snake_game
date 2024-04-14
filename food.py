from turtle import Turtle
import random


class Food:

    def __init__(self):
        self.food = None
        self.x = None
        self.y = None
        self.generate_food()

    def generate_food(self):
        self.x = random.randint(-470, 470)
        self.y = random.randint(-270, 270)
        self.food = Turtle()
        self.food.penup()
        self.food.shape('circle')
        self.food.color('white')
        self.food.goto(self.x, self.y) # x=470, y = 270
        # self.food.goto(480, 0)



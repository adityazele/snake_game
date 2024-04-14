from turtle import Turtle


class Scoreboard:

    def __init__(self):
        self.score = 0
        self.tim = Turtle()
        self.tim.penup()
        self.tim.hideturtle()
        self.tim.goto(0, 200)
        self.tim.color('white')
        self.tim.write(self.score, True, align='center', font=('Arial', 60, 'normal'))

    def update_score(self):
        self.score += 1
        self.tim.clear()
        self.tim.goto(0, 200)
        self.tim.write(self.score, True, align='center', font=('Arial', 60, 'normal'))


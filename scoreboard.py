
from turtle import Turtle


class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 240)
        self.score_count = -1
        self.score_point()


    def score_point(self):
        self.clear()
        self.score_count += 1
        self.write(f'Score: {self.score_count}', align='center', font=('Arial', 14, 'bold'))
        print(self.score_count)


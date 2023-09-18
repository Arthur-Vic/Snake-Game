
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')

class ScoreBoard(Turtle):


    def __init__(self, screen_size_y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, (screen_size_y/2)-50)
        self.score_count = 0
        self.update()

    def update(self):
        self.write(f'Score: {self.score_count}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)

    def score_point(self):
        self.clear()
        self.score_count += 1
        self.update()
        # print(self.score_count) Debugging


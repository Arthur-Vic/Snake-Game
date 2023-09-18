
from turtle import Turtle
import random


class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('yellow')
        self.speed('fastest')
        self.randomize()

    def randomize(self):
        food_x = random.randint(-275,275)
        food_y = random.randint(-275,275)
        self.goto(food_x, food_y)





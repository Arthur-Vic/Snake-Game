
from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():
    '''Input: start size for the snake body'''


    def __init__(self, snake_length):       
        self.snake_turtles = []
        self.create_snake(snake_length)
        self.head = self.snake_turtles[0]


    def create_snake(self, snake_length):
        for new_turtle_index in range(snake_length):
            new_turtle = Turtle()
            self.snake_turtles.append(new_turtle)
            new_turtle.penup()
            new_turtle.shape('square')
            new_turtle.color('white')
            new_turtle.goto(-20*new_turtle_index,0)


    def move(self):
        for turtle in range(len(self.snake_turtles) - 1, 0, -1):
            next_position = self.snake_turtles[turtle - 1].position()
            self.snake_turtles[turtle].goto(next_position)
            #print(next_position) Debugging
        self.head.forward(20)

    def grow(self):
        self.create_snake(1)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        



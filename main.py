
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('gray20')
screen.title('Python - Snake Game')
screen.tracer(0)

snake = Snake(4)
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

#screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    if snake.head.distance(food) < 20:
        food.randomize()
        snake.grow()
        scoreboard.score_point()
    snake.move()

screen.exitonclick()
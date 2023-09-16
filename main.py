
from turtle import Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('gray20')
screen.title('Python - Snake Game')
screen.tracer(0)

snake = Snake(4)

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

game_on = True
while game_on:
    screen.update()
    time.sleep(.07)
    snake.move()


screen.exitonclick()
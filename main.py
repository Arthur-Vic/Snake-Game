
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SCREEN_SIZE = [800, 800]

screen = Screen()
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.bgcolor('gray20')
screen.title('Python - Snake Game')
screen.tracer(0)

snake = Snake(4)
food = Food()
scoreboard = ScoreBoard(SCREEN_SIZE[1])

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

#screen.update()

game_on = True
while game_on:
    screen.update()
    time.sleep(.12 - scoreboard.score_count*0.007)

    # Food Collision
    if snake.head.distance(food) < 20:
        food.randomize()
        snake.grow()
        scoreboard.score_point()

    # # Wall Collision Mode
    # if snake.head.xcor() > (SCREEN_SIZE[0]/2)-20 or snake.head.xcor() < -((SCREEN_SIZE[0]/2)-20) or snake.head.ycor() > (SCREEN_SIZE[0]/2)-20 or snake.head.ycor() < -((SCREEN_SIZE[0]/2)-20):
    #     game_on = False
    #     scoreboard.game_over()

    # Wall PassThrough Mode
    if snake.head.xcor() > (SCREEN_SIZE[0]/2):
        snake.head.goto(-SCREEN_SIZE[0]/2, snake.head.ycor())
    if snake.head.xcor() < -(SCREEN_SIZE[0]/2):
        snake.head.goto(SCREEN_SIZE[0]/2, snake.head.ycor())
    if snake.head.ycor() > (SCREEN_SIZE[0]/2):
        snake.head.goto(snake.head.xcor(), -SCREEN_SIZE[0]/2)
    if snake.head.ycor() < -(SCREEN_SIZE[0]/2):
        snake.head.goto(snake.head.xcor(), SCREEN_SIZE[0]/2)

    # Collision with self
    for turtle in snake.snake_turtles[1:]:
        if snake.head.distance(turtle) < 10:
            game_on = False
            scoreboard.game_over()
        
    snake.move()


screen.exitonclick()
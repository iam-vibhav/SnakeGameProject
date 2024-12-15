from random import randint as ri
from turtle import Screen, Turtle
from snake import Snake
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Turtle("circle")
food.color("red")
food.penup()
food.goto(100, 100)

scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



def game_is_on():
    return (snake.head.xcor() <= 280 and snake.head.ycor() <= 280 and snake.head.xcor() >= -280 and snake.head.ycor() >= -280)

is_game_on = game_is_on()

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    if snake.head.distance(food) <= 20:
        food.goto(ri(-280,280),ri(-280,280))
        snake.increse()
        scoreboard.increse_score()

    if  not game_is_on():
        scoreboard.reset()
        time.sleep(1)
        snake.reset()


screen.exitonclick()






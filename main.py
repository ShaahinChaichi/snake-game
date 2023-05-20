from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(0.5)

screen.exitonclick()

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

x_position = [0, -20, -40, -10]
all_turtles = []

for turtle_index in range(0, 3):
    new_turtle = Turtle("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=x_position[turtle_index], y=0)
    all_turtles.append(new_turtle)

screen.exitonclick()

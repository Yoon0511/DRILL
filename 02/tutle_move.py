import turtle
import random

def move_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def move_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def move_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def move_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(move_up,'W')
turtle.onkey(move_left,'A')
turtle.onkey(move_down,'S')
turtle.onkey(move_right,'D')
turtle.onkey(restart,'Escape')

turtle.listen()

turtle.exitonclick()
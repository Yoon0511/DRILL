import turtle

count = 0

while count <= 6 :
    turtle.penup()
    turtle.goto(-100,-(int(count) * 100) + 200)
    turtle.pendown()
    turtle.forward(500)
    count = count + 1

count = 0

turtle.penup()
turtle.right(90)
turtle.pendown()

while count <= 6:
    turtle.penup()
    turtle.goto((int(count) * 100) - 100,200)
    turtle.pendown()
    turtle.forward(500)
    count = count + 1

turtle.exitonclick()
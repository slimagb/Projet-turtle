import turtle
import dessinMSDA

turtle.speed(10)

turtle.penup()
turtle.goto(0,20)
turtle.left(45)
turtle.pendown()
turtle.fillcolor("skyblue")
turtle.begin_fill()
dessinMSDA.rectangle(100, 50)
turtle.end_fill()

turtle.penup()
turtle.goto(0,20)
turtle.forward(100)
turtle.pendown()
turtle.fillcolor("skyblue")
turtle.begin_fill()
dessinMSDA.demi_cercle(25)
turtle.forward(100)
dessinMSDA.rectangle(100,50)
turtle.end_fill()

turtle.penup()
turtle.right(60)
turtle.pendown()
turtle.fillcolor("skyblue")
turtle.begin_fill()
turtle.forward(200)
turtle.left(60)
turtle.forward(35)
turtle.left(105)
turtle.forward(180)
turtle.end_fill()

turtle.penup()
turtle.left(80)
turtle.forward(85)
turtle.right(90)
turtle.forward(50)
turtle.right(30)
turtle.pendown()
turtle.fillcolor("skyblue")
turtle.begin_fill()
turtle.forward(200)
turtle.right(60)
turtle.forward(35)
turtle.right(105)
turtle.forward(180)
turtle.end_fill()

turtle.penup()
turtle.left(100)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.pendown()
turtle.fillcolor("skyblue")
turtle.begin_fill()
dessinMSDA.rectangle(100,50)
turtle.forward(100)
dessinMSDA.rectangle(65,50)
turtle.end_fill()

turtle.penup()
turtle.right(50)
turtle.pendown()
turtle.fillcolor("skyblue")
turtle.begin_fill()
turtle.forward(90)
turtle.left(60)
turtle.forward(30)
turtle.left(95)
turtle.forward(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-132,-112)
turtle.right(60)
turtle.pendown()
turtle.fillcolor("skyblue")
turtle.begin_fill()
turtle.forward(90)
turtle.right(60)
turtle.forward(30)
turtle.right(95)
turtle.forward(85)
turtle.end_fill()

turtle.penup()
turtle.goto(1000,1000)
turtle.pendown()

# turtle.penup()
# turtle.goto(0,20)
# turtle.pendown()


turtle.done()
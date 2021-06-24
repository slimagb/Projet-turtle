import turtle
import dessinMSDA

# chapeau
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
dessinMSDA.triangle(300)

# mur principal
turtle.penup()
turtle.goto(-75,-250)
turtle.pendown()
dessinMSDA.carre(250)

# porte
turtle.penup()
turtle.goto(-25,-240)
turtle.pendown()
dessinMSDA.rectangle(75, 150)

# pied
turtle.penup()
turtle.goto(-75,-250)
turtle.pendown()
dessinMSDA.rectangle(250,10)

# fenetre
turtle.penup()
turtle.goto(85, -110)
turtle.pendown()
dessinMSDA.carre(20)

turtle.penup()
turtle.goto(105, -110)
turtle.pendown()
dessinMSDA.carre(20)

turtle.penup()
turtle.goto(85, -130)
turtle.pendown()
dessinMSDA.carre(20)

turtle.penup()
turtle.goto(105, -130)
turtle.pendown()
dessinMSDA.carre(20)

# toil
turtle.penup()
turtle.goto(100,80)
turtle.pendown()
dessinMSDA.rectangle(20,50)



turtle.done()

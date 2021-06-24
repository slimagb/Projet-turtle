import math
import turtle

# définition des fontions
def cercle(rayon):
    turtle.circle(rayon)

def demi_cercle(rayon):
    turtle.circle(rayon, 180)

def carre(cote):
    for i in range(4):
        turtle.forward(cote)
        turtle.left(90)

def triangle(longueur):
    turtle.forward(longueur)
    turtle.left(135)
    turtle.forward(longueur/math.sqrt(2))
    turtle.left(90)
    turtle.forward(longueur/math.sqrt(2))
    turtle.left(135)

def rectangle(longueur, largeur):
    for i in range(2):
        turtle.forward(longueur)
        turtle.left(90)
        turtle.forward(largeur)
        turtle.left(90)

def polygone(cote, nb_cote):
    turtle.circle(cote, steps=nb_cote)

def trapeze(longueur, pB):
    turtle.forward(longueur/math.sqrt(2))
    turtle.forward(pB)
    turtle.forward(longueur / math.sqrt(2))
    turtle.left(135)
    turtle.forward(longueur)
    turtle.left(45)
    turtle.forward(pB)
    turtle.left(45)
    turtle.forward(longueur)
    turtle.left(135)

def losange(cote):
    turtle.left(90)
    turtle.forward(cote)
    turtle.left(120)
    turtle.forward(cote)
    turtle.left(60)
    turtle.forward(cote)
    turtle.left(120)
    turtle.forward(cote)

def ellipse(rayon):
    for i in range(2):
        turtle.circle(rayon, 90)
        turtle.circle(rayon/2, 90)
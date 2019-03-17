# Rafael Garcia
# April 25 2018
# This program makes a turtle walk 100 times randomly


import turtle
import random

roy = turtle.Turtle()
roy.speed(10)

for i in range(100):
    roy.forward(10)
    a = random.randrange(0, 359)
    roy.right(a)

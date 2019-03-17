#Rafael Garcia
#Feb 23 2018
#This program show the shades of green.


import turtle

turtle.colormode(255)
tess = turtle.Turtle()
tess.shape("turtle")
tess.backward(100)

#For 0,10,20,...,250
for i in range(0,255,10):
     tess.forward(10)
     tess.pensize(i)
     tess.color(0,i,0)
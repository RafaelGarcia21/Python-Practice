#Rafael Garcia79
#Feb 24 2018
#This program displays a purple turtle


import turtle

w = turtle.Screen()
purp = turtle.Turtle()
purp.shape("turtle")

c = input("Enter Hex Color: ")
purp.color(c)


w.exitonclick()
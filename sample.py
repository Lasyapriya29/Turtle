from turtle import Turtle, Screen
from random import choice,randint

t=Turtle()
s=Screen()
s.colormode(255)

t.shape("square")
t.color("red")

t.speed("fastest")

#generate random rgb color

def rcolor():
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    rc=(r,g,b)
    return rc

#spirograph

for _ in range(360//5):
    t.color(rcolor())
    t.circle(100)
    t.setheading(t.heading()+5)




#shapes

for i in range(3,10):
    t.color(rcolor())
    for j in range(i):
        t.forward(100)
        t.right(360//i)


s.exitonclick()

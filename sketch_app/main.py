from turtle import Turtle, Screen
from random import choice,randint

t=Turtle()
s=Screen()

def move_front():
    t.forward(10)

def move_back():
    t.backward(10)

def move_up():
    t.setheading(t.heading()+10)

def move_down():
    t.setheading(t.heading()-10)



def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(move_front,'w')
s.onkey(move_back,'s')
s.onkey(move_up,'d')
s.onkey(move_down,'a')
s.onkey(clear,'c')

s.exitonclick()

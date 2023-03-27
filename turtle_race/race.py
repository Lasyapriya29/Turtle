from turtle import Turtle, Screen
from random import choice,randint

s=Screen()

race=False
s.setup(width=500,height=400)
select_turtle=s.textinput(title=
                             "Select your turtle ", prompt='''Enter a color from the below colors:
"red" "orange" "yellow" "green" "blue" "purple:''')
colors=["red","orange","green","blue","purple"]
all_turtles=[]

k=0
for i in range(0,5):
    t=Turtle(shape="turtle")
    t.penup()
    t.goto(x=-230,y=-100+k)
    t.color(colors[i])
    k+=40
    all_turtles+=[t]

if select_turtle:
    race=True

while race:
    for t in all_turtles:
        if t.xcor()>230:
            race=False
            if t.pencolor()==select_turtle:
                print(f"{select_turtle} Your turtle won the race!")
            else:
                print(f"{select_turtle} Your turtle lost the race!")
        rand_dist=randint(0,10)
        t.forward(rand_dist)

s.exitonclick()

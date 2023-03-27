from turtle import Turtle
POSITIONS=[(0,0),(-15,0),(-30,0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for p in POSITIONS:
            self.add_segment(p)

    def add_segment(self,p):
        segment=Turtle("circle")
        segment.color("white")
        segment.penup()
        segment.goto(p)
        self.segments+=[segment]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(0)
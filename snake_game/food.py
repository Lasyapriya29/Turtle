from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
        self.color("saddle brown")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x=randint(-270,270)
        rand_y=randint(-270,270)
        self.goto(rand_x,rand_y)
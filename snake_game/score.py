from turtle import Turtle
ALIGN="center"
FONT=("Courier",24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}",align=ALIGN,font=FONT)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGN,font=FONT)
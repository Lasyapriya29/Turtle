from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

s=Screen()
s.setup(width=600,height=600)
s.bgcolor("green")
s.title("Snake Game")
s.tracer(0)

snake=Snake()
food=Food()
score=Score()
s.listen()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game=True
while game:
    s.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score.increase_score()


    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game=False
        score.game_over()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            game=False
            score.game_over()



s.exitonclick()
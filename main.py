import time
from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard
s1 = Screen()
s1.setup(width=600, height=600)
s1.bgcolor("black")
s1.title("My Snake Game")
s1.tracer(0)

t1 = Snake()
f1 = Food()
scoreboard = Scoreboard()
s1.listen()
s1.onkey(key ="Up",fun = t1.up)
s1.onkey(key ="Down",fun = t1.down)
s1.onkey(key ="Right",fun = t1.right)
s1.onkey(key ="Left",fun = t1.left)
game_is_on = True

while game_is_on:
    s1.update()
    time.sleep(0.1)
    t1.part2()
    #detect collision with food
    x = t1.head.xcor()
    y = t1.head.ycor()
    if x > 290 or x < -290 or y > 290 or y < -290:
        scoreboard.game_over()
        game_is_on = False
    else:
        if t1.head.distance(f1) < 15:
            f1.refresh()
            t1.extend()
            scoreboard.increase_score()
        for segments in t1.body[1:]:
            # if segments == t1.head:
            #     pass
            if t1.head.distance(segments) < 15:
                scoreboard.game_over()
                game_is_on = False
s1.exitonclick()

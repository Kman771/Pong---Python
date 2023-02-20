from turtle import Screen, Turtle
import random

import ball_class
import paddle
from paddle import Paddle
from ball_class import Ball
from score import Score
import time
speed = 0.15
# Screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong Game by Kaashish")
screen.tracer(0)

# Paddle
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

# Ball
ball = Ball()

# Score
score = Score()

screen.listen()

screen.onkey(paddle1.move_forward, "Up")
screen.onkey(paddle1.move_backward, "Down")
screen.onkey(paddle2.move_forward, "w")
screen.onkey(paddle2.move_backward, "s")

line = Turtle()
line.hideturtle()
line.penup()
line.goto(0, 240)
line.setheading(270)
for i in range(20):
    line.pendown()
    line.color("white")
    line.pensize(5)
    line.forward(20)
    line.penup()
    line.forward(20)


game_on = True
while game_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    time.sleep(speed)

    if ball.distance(paddle1) < 50 and 370 > ball.xcor() >= 320:
        if ball.xcor() < 350:
            if 35 > ball.ycor() - paddle1.ycor() > -35:
                ball.bounce_paddle()
                speed *= 0.9
                paddle.increment += 0.5
                ball.angle += 5
            else:
                ball.bounce_back()
                speed *= 0.9
                paddle.increment += 0.5
                ball.angle += 5

        else:
            ball.bounce()

    if ball.distance(paddle2) < 50 and -370 < ball.xcor() <= -320:
        if ball.xcor() > -350:
            if -35 < ball.ycor() - paddle2.ycor() < 35:
                ball.bounce_paddle()
                speed *= 0.9
                paddle.increment += 0.5
                ball.angle += 5
            else:
                ball.bounce_back()
                speed *= 0.9
                paddle.increment += 0.5
                ball.angle += 5
        else:
            ball.bounce()

    if ball.xcor() > 420:
        score.add_score_p2()
        time.sleep(0.7)
        ball = Ball()
        paddle1.position()
        paddle.increment = 30
        ball.angle = random.choice(ball_class.ANGLES)
        speed = 0.1

    elif ball.xcor() < -420:
        score.add_score_p1()
        time.sleep(0.5)
        ball = Ball()
        paddle.increment = 30
        ball.angle = random.choice(ball_class.ANGLES)
        speed = 0.1

    if score.number1 > 11 or score.number2 > 11:
        game_on = False


screen.exitonclick()

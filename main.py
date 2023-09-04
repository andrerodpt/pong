from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)


## Paddles init
right_paddle_pos = (350, 0)
right_paddle = Paddle(position=right_paddle_pos)
left_paddle_pos = (-350, 0)
left_paddle = Paddle(position=left_paddle_pos)

## Ball init
ball = Ball()

## Scoreboard init
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=right_paddle.go_up, key='Up')
screen.onkey(fun=right_paddle.go_down, key='Down')
screen.onkey(fun=left_paddle.go_up, key='w')
screen.onkey(fun=left_paddle.go_down, key='s')


game_is_on = True
while game_is_on:
    ball.move()
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collision with walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce('wall')

    # Detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce('paddle')

    # Detect out of bounds (right side)
    if ball.xcor() >= 380:
        ball.reset()
        scoreboard.l_point()

    # Detect out of bounds (left side)
    if ball.xcor() <= -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
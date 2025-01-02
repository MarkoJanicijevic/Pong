from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(1600, 1000)
screen.listen()
screen.tracer(0)




left_paddle = Paddle((-750, 0))
right_paddle = Paddle((750, 0))
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

scoreboard = ScoreBoard()

game_is_on = True

ball = Ball()

x = 10
y = 10


while game_is_on:
    screen.update()
    ball.move_ball(x, y)
    time.sleep(0.1)
    #collision with top and bottom
    if ball.ycor() > 490 or ball.ycor() < -490:
        y *= -1

    if ball.distance(left_paddle) < 50 and ball.xcor() < -730 or ball.distance(right_paddle) < 50  and ball.xcor() > 730:
        x *= -1


    if ball.xcor() > 790:
        ball.reset_position()
        scoreboard.r_point()
    elif  ball.xcor() < -790:
        ball.reset_position()
        scoreboard.l_point()





left_paddle.move_up()































screen.exitonclick()
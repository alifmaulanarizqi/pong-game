from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_PADDLE_POS = (350, 0)
L_PADDLE_POS = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(R_PADDLE_POS)
l_paddle = Paddle(L_PADDLE_POS)

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)


is_game_over = False
while not is_game_over:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # Ball collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Ball collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    # Right paddle miss
    if ball.xcor() > 380:
        scoreboard.increment_l_score()
        ball.reset()

    # Left paddle miss
    if ball.xcor() < -380:
        scoreboard.increment_r_score()
        ball.reset()


screen.exitonclick()

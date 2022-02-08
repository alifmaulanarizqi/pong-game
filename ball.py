from turtle import Turtle
import random

DIRECTION = [-10, 10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = random.choice(DIRECTION)
        self.y_move = random.choice(DIRECTION)
        self.move_speed = 0.07

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.bounce_paddle()
        self.y_move = random.choice(DIRECTION)
        self.goto(0, 0)
        self.move_speed = 0.07

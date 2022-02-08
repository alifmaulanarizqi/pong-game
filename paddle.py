from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        old_x = self.xcor()
        new_y = self.ycor() + 30
        self.goto(old_x, new_y)

    def down(self):
        old_x = self.xcor()
        new_y = self.ycor() - 30
        self.goto(old_x, new_y)

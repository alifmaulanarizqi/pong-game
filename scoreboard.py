from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-5, 230)
        self.write(f"{self.l_score} : ", align="center", font=("Courier", 40, "normal"))
        self.goto(70, 230)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def increment_l_score(self):
        self.l_score += 1
        self.update_score()

    def increment_r_score(self):
        self.r_score += 1
        self.update_score()

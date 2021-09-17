from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.write(f"Level : {self.score}", False, align="left", font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"Level : {self.score}", False, align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 150)
        self.write(f"Game Over", False, align="center", font=FONT)

from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250,250)
        self.level = 0


    def update(self):

        self.clear()
        self.level += 1
        self.write(arg = f"Level: {self.level}",align = "left",font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=FONT)
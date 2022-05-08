from turtle import Turtle

with open("score.txt", mode="r") as file:
    sc = int(file.read())

ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = sc
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=275)
        self.write(f"Your Score: {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Your Score: {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_highscore(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"Your Score: {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

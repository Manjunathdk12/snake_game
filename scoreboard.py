from turtle import Turtle

ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 230)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Arial", 10, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align=ALIGNMENT, font=("Arial", 10, "normal"))

    def increment(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

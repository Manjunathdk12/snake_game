from turtle import Turtle
from scoreboard import Scoreboard
final_score=Scoreboard

class Game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))


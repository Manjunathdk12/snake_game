import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.y = None
        self.x = None
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.color("yellow")
        self.refresh()

    def refresh(self):

        self.x = random.randint(-230, 230)
        self.y = random.randint(-230, 230)
        self.goto(self.x, self.y)

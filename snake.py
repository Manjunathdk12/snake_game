from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        my_turtle = Turtle(shape="square")
        my_turtle.color("white")
        my_turtle.penup()
        my_turtle.goto(position)
        self.full_snake.append(my_turtle)

    def extend(self):
        self.add_segment(self.full_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.full_snake) - 1, 0, -1):
            x_cor = self.full_snake[seg_num - 1].xcor()
            y_cor = self.full_snake[seg_num - 1].ycor()
            self.full_snake[seg_num].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

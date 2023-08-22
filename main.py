from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard

score = Scoreboard()
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
screen.listen()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increment()
    # detect collision with wall
    if snake.head.xcor() > 240 or snake.head.xcor() < -240 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
        game_is_on = False
        score.game_over()

    for segment in snake.full_snake[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
screen.exitonclick()

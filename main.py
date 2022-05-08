from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

new_snake = Snake()
new_food = Food()
new_score = Scoreboard()

screen.listen()

screen.onkey(fun=new_snake.up, key="Up")
screen.onkey(fun=new_snake.down, key="Down")
screen.onkey(fun=new_snake.left, key="Left")
screen.onkey(fun=new_snake.right, key="Right")

start_game = True

while start_game:
    screen.update()
    time.sleep(.1)

    new_snake.move_snake()
    if new_snake.head.distance(new_food) < 15:
        new_snake.update_snake()
        new_score.update_score()
        new_food.new_food_element()

    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        new_score.reset_highscore()
        new_snake.reset_snake()
    for snake_body in new_snake.snake_list[1:]:
        if new_snake.head.distance(snake_body) < 10:
            new_score.reset_highscore()
            new_snake.reset_snake()


screen.exitonclick()

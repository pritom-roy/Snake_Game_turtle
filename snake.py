from turtle import Turtle

POSITION_LIST = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in POSITION_LIST:
            self.extend(position)

    def extend(self, position):
        swa = Turtle()
        swa.penup()
        swa.color("white")
        swa.shape("square")
        swa.goto(position)
        self.snake_list.append(swa)

    def reset_snake(self):
        for element in self.snake_list:
            element.goto(x=1000., y=1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]

    def update_snake(self):
        self.extend(self.snake_list[-1].position())

    def move_snake(self):
        for key in range(len(self.snake_list) - 1, 0, -1):
            x_cor = self.snake_list[key - 1].xcor()
            y_cor = self.snake_list[key - 1].ycor()

            self.snake_list[key].goto(x=x_cor, y=y_cor)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # self.snake_list[0].left(90) Work as same

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

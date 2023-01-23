from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            snake_part = Turtle("square")
            snake_part.color('white')
            snake_part.penup()
            snake_part.goto(position)
            self.snake_parts.append(snake_part)

    def move(self):
        for idx in range(len(self.snake_parts) - 1, 0, -1):
            curr_x = self.snake_parts[idx - 1].xcor()
            curr_y = self.snake_parts[idx - 1].ycor()
            self.snake_parts[idx].goto(curr_x, curr_y)
        self.snake_parts[0].forward(MOVE_DISTANCE)


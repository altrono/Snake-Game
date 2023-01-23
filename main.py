from turtle import Screen, Turtle
import time
# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Anaconda Snake Game')
# .tracer(0) so that it keeps the screen blank until we call the method .update()
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]

my_snake_list = []

for position in starting_position:
    new_turtle = Turtle("square")
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.goto(position)
    my_snake_list.append(new_turtle)

# To make screen elements visible
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.5)
    # make our snake move forward
    for idx in range(len(my_snake_list) - 1, 0, -1):
        new_x = my_snake_list[idx - 1].xcor()
        new_y = my_snake_list[idx - 1].ycor()
        my_snake_list[idx].goto(new_x, new_y)
    my_snake_list[0].forward(20)

    my_snake_list[0].left(90)

    # [s1,s2,s3]









screen.exitonclick()
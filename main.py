from turtle import Screen, Turtle

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Anaconda Snake Game')


starting_position = [(0, 0), (-20, 0), (-40, 0)]
my_snake_list = []
for position in starting_position:
    new_turtle = Turtle("square")
    new_turtle.color('white')
    new_turtle.goto(position)
    my_snake_list.append(new_turtle)




screen.exitonclick()
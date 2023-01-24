from turtle import Screen
import time
from snake import Snake
from food import Food
# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Anaconda Snake Game')
# .tracer(0) so that it keeps the screen blank until we call the method .update()
screen.tracer(0)

snake = Snake()
food = Food()

# The screen starts listening to some key press
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

screen.exitonclick()
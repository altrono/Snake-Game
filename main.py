from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Anaconda Snake Game')
# .tracer(0) so that it keeps the screen blank until we call the method .update()
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

# The screen starts listening to some key press
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.2)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.reset()

    # Detect collision with its own body
    for seg in snake.snake_parts[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset()
            score.reset()



screen.exitonclick()
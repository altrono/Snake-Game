import random
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open('score.txt', 'r') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()



    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(f' GAME OVER \nFinal score: {self.score}', align=ALIGNMENT, font=FONT)





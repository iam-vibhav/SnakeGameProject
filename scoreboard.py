from turtle import Turtle

ALIGNMENT = "centre"
FONT = ("Arial", 30, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
         super().__init__()
         self.score = 0
         self.highscore = 0
         self.color("white")
         self.penup()
         self.goto(0,260)
         self.update_score()
         self.hideturtle()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}   High Score : {self.highscore}", False, "center", FONT)

    def increse_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_score()
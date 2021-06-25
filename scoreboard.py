from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 3
        self.color("black")
        self.penup()
        self.goto(-250,270)
        self.write(f"Score: {self.score}|{self.life} life left", False, align="center", font=(FONT))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}|{self.life} life left", False, align="center", font=(FONT))

    def reduce_life(self):
        self.clear()
        self.life -= 1
        self.write(f"Score: {self.score}|{self.life} life left", False, align="center", font=(FONT))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over!!\nYour score: {self.score}", False, align="center", font=(FONT))
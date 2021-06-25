from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.goto(random.randint(300,1000), random.randint(-200,200))
        self.shapesize(stretch_wid=0.7, stretch_len=2)
        self.move_distance = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() - self.move_distance
        self.goto(new_x,self.ycor())

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
        self.move()

    def car_reset(self):
        self.goto(random.randint(300,1000), random.randint(-200,200))




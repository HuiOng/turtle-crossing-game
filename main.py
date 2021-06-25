import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = []
for _ in range(20):
    car = CarManager()
    cars.append(car)


screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    for car in cars:
        car.move()
        if car.xcor()< -300:
            car.car_reset()
            car.move()
    screen.update()

    #detect score
    if player.ycor() > 300:
        scoreboard.update_score()
        player.reset_position()
        for car in cars:
            car.car_reset()
            car.increase_speed()

    #detect collision with car
    for car in cars:
        if car.distance(player)< 20:
            player.reset_position()
            scoreboard.reduce_life()

    if scoreboard.life == 0:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
screen.listen()
car = CarManager()
score = Scoreboard()
score.update()
screen.onkey(fun = player.move, key="Up")
count =0
while game_is_on:
    count +=1
    time.sleep(0.1)
    car.move()
    screen.update()
    if count == 6:
        car.create()
        count = 0
    # car.move()

    if player.ycor() > 280:
        player.reset()
       
        score.update()
        car.increase_speed()
    if car.check_impact(player):
        score.game_over()
        break
    # score.game_over()
screen.exitonclick()

from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):

        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create()
        # while(True):
        #     self.forward(STARTING_MOVE_DISTANCE)

    def create(self):
        new_tur = Turtle("square")
        new_tur.shapesize(stretch_wid=1, stretch_len=2)
        new_tur.penup()
        new_tur.goto(300, random.randint(-250, 250))
        new_tur.color(random.choice(COLORS))
        new_tur.setheading(180)

        self.all_cars.append(new_tur)

    def move(self):
        for item in self.all_cars:
            item.forward(self.move_distance)
            if item.xcor()< -330:
                item.clear()

    def increase_speed(self):
        self.move_distance = self.move_distance + MOVE_INCREMENT

    def check_impact(self,player):
        for item in self.all_cars:
            if item.distance(player) < 20 :
                return True
        return False


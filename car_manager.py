from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_CAR_X = 300
COLLISION_DISTANCE = 20
MAX_CARS = 20


class Car(Turtle):
    def __init__(self, color, position, move_distance):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.setpos(x=position[0], y=position[1])
        self.seth(180)
        self.move_distance = move_distance

    def move(self):
        self.forward(self.move_distance)


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def add_car(self):
        color = random.choice(COLORS)
        start_y = random.randint(-280, 280)
        self.cars.append(
            Car(color, (START_CAR_X, start_y), self.move_distance))

    def move_cars(self):
        for car in self.cars:
            car.move()

    def hit_car(self, player):
        for car in self.cars:
            if (player.distance(car) < COLLISION_DISTANCE):
                return True
        return False

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
        for car in self.cars:
            car.move_distance = self.move_distance

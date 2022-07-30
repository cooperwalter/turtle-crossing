import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from datetime import datetime, timedelta

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
manager = CarManager()

screen.onkey(key="Up", fun=player.up)

last_car_spawn_time = datetime.now()
print(last_car_spawn_time)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    manager.move_cars()
    # manager.clear_exited_cars()
    if manager.hit_car(player):
        game_is_on = False

    # if manager.can_add_car():
    #     manager.add_car()

    now = datetime.now()
    delta = timedelta(seconds=0.5)
    if (now - delta > last_car_spawn_time):
        manager.add_car()
        last_car_spawn_time = now

    if player.ycor() > 280:
        player.reset()
        scoreboard.increment_level()
        manager.increase_speed()

scoreboard.game_over()
screen.exitonclick()

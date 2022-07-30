from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-220, 260)
ALIGNMENT = "center"
GAME_OVER_POSITION = (0, 0)


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(SCORE_POSITION)
        self.color('black')
        self.level = 1
        self.draw_level()

    def draw_level(self):
        self.clear()
        self.setpos(SCORE_POSITION)
        self.write(f"Level: {self.level}", font=FONT, align=ALIGNMENT)

    def increment_level(self):
        self.level += 1
        self.draw_level()

    def game_over(self):
        self.setpos(GAME_OVER_POSITION)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)

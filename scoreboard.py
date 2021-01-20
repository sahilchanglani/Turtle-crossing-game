from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        with open("highscore.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.display()

    def display(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        self.goto(280, 260)
        self.write(f"Highscore: {self.high_score}", align="right", font=FONT)

    def level_up(self):
        self.level += 1
        self.display()

    def game_over(self):
        if self.level > self.high_score:
            self.high_score = self.level
            with open("highscore.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.display()
            self.goto(0, -50)
            self.write("New High-score!!", align="center", font=FONT)
        self.home()
        self.write("GAME OVER", align="center", font=("Courier", 40, "normal"))



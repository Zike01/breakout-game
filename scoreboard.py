from turtle import Turtle

FONT = ('Pixeboy', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.num_lives = 3
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, 270)
        self.write(f'Score: {self.score}', align='center', font=FONT)

        self.goto(270, 270)
        self.write(f'Lives : {self.num_lives}', align='center', font=FONT)

    def increase_score(self, num_points):
        self.score += num_points
        self.update_scoreboard()

    def lose_life(self):
        self.num_lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)

    def completed(self):
        self.goto(0, 0)
        self.write('Thanks for Playing!', align='center', font=FONT)

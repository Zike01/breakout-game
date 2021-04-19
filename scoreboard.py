from turtle import Turtle
FONT = ('Pixeboy', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.num_lives = 3
        self.color('white')
        self.hideturtle()
        self.penup()

        self.score = 0
        # Read and display the high score from data.txt
        with open('data.txt') as data:
            self.high_score = int(data.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 270)
        self.write(f'Score: {self.score}   High Score {self.high_score}', align='center', font=FONT)

        self.goto(270, 270)
        self.write(f'Lives : {self.num_lives}', align='center', font=FONT)

    def increase_score(self, num_points):
        self.score += num_points
        self.update_scoreboard()

    def lose_life(self):
        self.num_lives -= 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        # Store the high score in data.txt
        if self.score > self.high_score:
            with open('data.txt', mode='w') as data:
                data.write(f"{self.score}")

    def completed(self):
        self.goto(0, 0)
        self.write('Thanks for Playing!', align='center', font=FONT)
        self.reset_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)
        self.reset_scoreboard()

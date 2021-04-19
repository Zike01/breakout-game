from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(position)

    def move_right(self):
        # Add paddle boundaries
        if self.xcor() < 220:
            self.forward(30)

    def move_left(self):
        if self.xcor() > -220:
            self.backward(30)

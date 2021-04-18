from turtle import Turtle


class Bricks:
    def __init__(self):
        self.brick_objects = []
        self.rows_filled = 0

        for y in range(100, 260, 20):
            for x in range(-300, 301, 50):
                new_brick = Turtle()
                new_brick.shape("square")
                new_brick.shapesize(stretch_wid=0.5, stretch_len=2)
                new_brick.penup()
                new_brick.goto(x, y)

                # Change color depending on the number of rows filled (different color every 2 rows)
                if self.rows_filled < 2:
                    new_brick.color('yellow')
                elif self.rows_filled < 4:
                    new_brick.color('green')
                elif self.rows_filled < 6:
                    new_brick.color('orange')
                else:
                    new_brick.color('red')

                # Add the new brick to the brick_objects list
                self.brick_objects.append(new_brick)

            self.rows_filled += 1

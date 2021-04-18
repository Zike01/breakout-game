from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
import time

# Create Screen
screen = Screen()
screen.setup(width=650, height=600)
screen.bgcolor("black")
screen.title("Atari BREAKOUT")
screen.tracer(0)


# Create paddle object
paddle = Paddle((0, -200))

# Create ball object
ball = Ball()

# Create bricks
bricks = Bricks()

# Create scoreboard
scoreboard = Scoreboard()


# Move paddle left and right
screen.listen()
screen.onkeypress(paddle.move_right, "Right")
screen.onkeypress(paddle.move_left, "Left")

num_of_hits = 0

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.xcor() > 305 or ball.xcor() < -305:
        ball.bounce_x()

    if ball.ycor() > 280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle) < 120 and ball.ycor() < -170:
        ball.bounce_y()

    # Detect collision with bricks
    for brick in bricks.brick_objects:
        if ball.distance(brick) < 20:
            ball.bounce_y()
            brick.hideturtle()
            bricks.brick_objects.remove(brick)

            # Check color of brick knocked down and add appropriate points
            if brick.color()[0] == 'red':
                num_points = 7
                ball.increase_speed()

            elif brick.color()[0] == 'orange':
                num_points = 5
                ball.increase_speed()

            elif brick.color()[0] == 'green':
                num_points = 3
            else:
                num_points = 1

            scoreboard.increase_score(num_points)

    # Increase speed after 4 and 12 hits
    if num_of_hits == 4 or num_of_hits == 12:
        ball.increase_speed()

    # Detect out of bounds // Lose a life
    if ball.ycor() < -280:
        ball.restart()
        num_of_hits = 0  # Reset the number of hits
        scoreboard.lose_life()

    # Detect lives lost
    if scoreboard.num_lives == 0:
        scoreboard.game_over()
        game_is_on = False

    # Detect if all bricks removed
    if len(bricks.brick_objects) == 0:
        scoreboard.completed()
        game_is_on = False


screen.exitonclick()

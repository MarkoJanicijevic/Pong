from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.ball_heading = 1
        self.pace = 0.1


    def move_ball(self, x, y):
        new_x = self.xcor() + x * self.ball_heading
        new_y = self.ycor() + y
        self.goto((new_x, new_y))

    def increase_pase(self):
        self.pace *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.ball_heading *= -1
        self.pace = 0.1
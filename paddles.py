from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.create_paddle()



    def create_paddle(self):
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.goto(self.pos)

    def move_up(self):
        x = self.xcor()
        y = self.ycor() + 30
        self.goto(x, y)

    def move_down(self):
        x = self.xcor()
        y = self.ycor() - 30
        self.goto(x, y)





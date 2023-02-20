from turtle import Turtle

DISTANCE = 20
increment = 30


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.shape("square")
        self.goto(position)

    def move_forward(self):
        new_ycor = self.ycor() + increment
        self.goto(self.xcor(), new_ycor)

    def move_backward(self):
        new_ycor = self.ycor() - increment
        self.goto(self.xcor(), new_ycor)



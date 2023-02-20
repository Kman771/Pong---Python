from turtle import Turtle
import random

ANGLES = [30, 60, 45, 120, 135, 150, 210, 225, 240, 300, 315, 330]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.angle = random.choice(ANGLES)

    def move(self):
        self.setheading(self.angle)
        self.forward(30)

    def bounce(self):
        self.angle = 360 - self.angle

    def bounce_paddle(self):
        self.angle = (360 - self.angle) + 180

    def bounce_back(self):
        if self.angle > 180:
            self.angle -= 180
        else:
            self.angle = 180 - self.angle











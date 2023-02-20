from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.number1 = 0
        self.number2 = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.write(f"{self.number2} - {self.number1}", False, "center", ("Arial", 25, "normal"))

    def add_score_p1(self):
        self.number1 += 1
        self.clear()
        self.write(f"{self.number2} - {self.number1}", False, "center", ("Arial", 25, "normal"))

    def add_score_p2(self):
        self.number2 += 1
        self.clear()
        self.write(f"{self.number2} - {self.number1}", False, "center", ("Arial", 25, "normal"))

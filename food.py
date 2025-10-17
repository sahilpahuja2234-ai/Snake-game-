from turtle import Turtle
import random
wn = Turtle()
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.5, 0.5, 1)
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        a = random.randint(-280, 280)
        b = random.randint(-280, 280)
        self.goto(a, b)
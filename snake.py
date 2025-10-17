from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body = []
        self.x = 3
        self.steps = 20
        self.make_a_body()
        self.head = self.body[0]

    def make_a_body(self):
        for i in range(self.x):
            self.add((-20 * i, 0))

    def add(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.speed("fastest")
        new_turtle.penup()
        new_turtle.goto(position)
        self.body.append(new_turtle)

    def extend(self):
        self.add(self.body[-1].position())

    def part2(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.forward(self.steps)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

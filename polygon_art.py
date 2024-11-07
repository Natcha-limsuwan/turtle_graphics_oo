import turtle
import random

choice = int(input('Which art do you want to generate?'
                   '\nEnter a number between 1 to 9 inclusive: '))


class Turtle:
    def __init__(self, choice):
        self.num_side = self.num_side()
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.border_size = random.randint(1, 10)
        self.color = self.get_new_color()
        self.reduction_ratio = 0.618
        self.choice = choice

    def num_side(self):
        if choice in [1, 2, 3]:
            num_side = choice + 2
            self.choice = num_side
            return self.choice
        elif choice in [4, 8, 9]:
            num_side = random.randint(3, 5)
            self.choice = num_side
            return self.choice
        else:
            num_side = choice - 2
            self.choice = num_side
            return self.choice

    def other_choice(self):
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - self.reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= self.reduction_ratio
        turtle.penup()

    def draw(self):
        for i in range(3):
            self.draw_polygon()
            if choice == 9:
                self.other_choice()
            elif 5 <= choice <= 9:
                self.other_choice()

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_side):
            turtle.forward(self.size)
            turtle.left(360 / self.num_side)
        turtle.penup()

    def get_new_color(self):
        self.new_color = (random.randint(0, 255), random.randint(0, 255),
                          random.randint(0, 255))
        return self.new_color

    turtle.speed(0)
    turtle.bgcolor('black')
    turtle.tracer(0)
    turtle.colormode(255)


if 1 <= choice <= 7:
    for i in range(20):
        drawing = Turtle(choice)
        drawing.draw()
if choice == 8:
    for i in range(2):
        for j in range(15):
            drawing = Turtle(choice)
            drawing.draw()
        drawing = Turtle(choice)
        drawing.draw_polygon()
if choice == 9:
    for i in range(15):
        drawing = Turtle(choice)
        drawing.draw()
    drawing = Turtle(choice)
    drawing.draw_polygon()
turtle.done()

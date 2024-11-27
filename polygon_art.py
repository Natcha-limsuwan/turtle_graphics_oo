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

'''import turtle
import random

class PolygonArt():
	def __init__(self, n) -> None:
		self.__n = n

	@property
	def n(self):
		return self.__n

	@n.setter
	def n(self, n):
		self.__n = n


	def run(self):
		for _ in range(30):
			n_sides  = 3
			if self.__n in [4, 8, 9]:
				n_sides  = random.randint(3, 5)
			if self.__n in [2, 6]:
				n_sides  = 4
			if self.__n in [3, 7]:
				n_sides  = 5
			if 5 <= self.__n <= 9:
				depth = 3
				if self.__n == 9:
					depth = random.randint(0, 3)
				polygon = EmbeddedPolygon(n_sides, depth)
				polygon.draw()
			else:
				polygon = Polygon(n_sides)
				polygon.draw()


class Polygon():
	def __init__(self, n_sides) -> None:
		self.__num_sides = n_sides
		self.__size = random.randint(50, 150)
		self.__orientation = random.randint(0, 90)
		self.__location = [random.randint(-300, 300), random.randint(-200, 200)]
		self.__color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
		self.__border_size = random.randint(1, 10)

	@property
	def size(self):
		return self.__size

	@size.setter
	def size(self, value):
		self.__size = value

	@property
	def num_sides(self):
		return self.__num_sides

	@property
	def location(self):
		return self.__location

	@property
	def orientation(self):
		return self.__orientation

	@property
	def color(self):
		return self.__color

	@property
	def border_size(self):
		return self.__border_size

	def draw(self):
		turtle.penup()
		turtle.goto(self.location[0], self.location[1])
		turtle.setheading(self.orientation)
		turtle.color(self.color)
		turtle.pensize(self.border_size)
		turtle.pendown()
		self.move()
		turtle.penup()

	def move(self):
		for _ in range(self.num_sides):
			turtle.forward(self.size)
			turtle.left(360/self.num_sides)

class EmbeddedPolygon(Polygon):
	def __init__(self, n_sides, depth):
		super().__init__(n_sides)
		self.__ratio = 0.618
		self.__depth = depth

	@property
	def ratio(self):
		return self.__ratio

	@property
	def depth(self):
		return self.__depth

	def draw(self):
		for _ in range(1, self.__depth + 1):
			turtle.penup()
			turtle.goto(self.location[0], self.location[1])
			turtle.setheading(self.orientation)
			turtle.right(90 + (180/self.num_sides))
			turtle.forward((self.size / self.__ratio) - self.size)
			turtle.color(self.color)
			turtle.pensize(self.border_size)
			turtle.pendown()
			turtle.setheading(self.orientation)
			self.move()
			self.size *= self.__ratio
			turtle.penup()


turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

while(True):
	n = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
	turtle.clear()
	if n == 0:
		break
	elif 1 <= n <= 9:
		art = PolygonArt(n)
		art.run()
	else:
		print("Please try again")

turtle.done()
message.txt'''

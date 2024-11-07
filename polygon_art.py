import turtle
import random

class Polygon:

    def __init__(self,num_sides=0, size=0, orientation=0, location=[0,0], color=(0,0,0), border_size=0) -> None:
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)


    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()


    def draw_shape(self,num_sides=0):
        if num_sides == 0:
            self.num_sides = random.randint(3, 5)
        else:
            self.num_sides = num_sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)
        self.draw_polygon()


    def change_pos(self):
        reduction_ratio = 0.618
        turtle.penup()
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= reduction_ratio
        self.draw_polygon()


class Polygon_choice:

    choice = int(input("Write the choice you want (1-9): "))
    a = Polygon()
    if choice == 1:
        for _ in range(random.randint(25,35)):
            a.draw_shape(num_sides=3)
    elif choice == 2:
        for _ in range(random.randint(25,35)):
            a.draw_shape(num_sides=4)
    elif choice == 3:
        for _ in range(random.randint(25,35)):
            a.draw_shape(num_sides=5)
    elif choice == 4:
        for _ in range(random.randint(15,25)):
            a.draw_shape()
    elif choice == 5:
        for _ in range(random.randint(25,35)):
            a.draw_shape(num_sides=3)
            for _ in range(2):
                a.change_pos()
    elif choice == 6:
        for _ in range(random.randint(25,35)):
            a.draw_shape(num_sides=4)
            for _ in range(2):
                a.change_pos()
    elif choice == 7:
        for _ in range(random.randint(25,35)):
            a.draw_shape(num_sides=5)
            for _ in range(2):
                a.change_pos()
    elif choice == 8:
        for _ in range(random.randint(15,25)):
            a.draw_shape()
            for _ in range(2):
                a.change_pos()
    elif choice == 9:
        for _ in range(random.randint(15,25)):
            a.draw_shape()
            for _ in range(random.randint(0,2)):
                a.change_pos()

    turtle.done()
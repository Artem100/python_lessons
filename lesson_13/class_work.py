from math import sqrt


class Figure():

    def P(self):
        raise Exception

    def S(self):
        raise Exception

class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def P(self):
        P = self.a + self.b + self.c
        print(P)

    def S(self):
        S = 0.5*(self.a + self.b + self.c)
        print(S)

class Rectangle(Figure):

    def __init__(self, a_b):
        self.a_b = a_b

    def P(self):
        P = 2*(self.a_b[0] + self.a_b[1])
        print(P)

    def S(self):
        S = self.a_b[0]* self.a_b[1]
        print(S)

class Circle(Figure):

    def __init__(self, a):
        self.a = a
        self.radius = a/(2*3.14)

    def P(self):
        P = 3.14*self.radius*2
        print(P)

    def S(self):
        S = 3.14*(self.radius**2)
        print(S)

class Point(Figure):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def P(self):
        P = sqrt((self.x[0]-self.x[1])**2+(self.y[0]-self.y[1])**2)
        print(P)

    def S(self):
        S = ((self.x+self.y)/2)*sqrt(self.x*self.y)
        print(S)

# class Polygon(Figure):
#
#
#

# triangle = Triangle(3, 4)
# triangle.P()
# triangle.S()

# rectangle = Rectangle([3, 6])
# rectangle.P()
# rectangle.S()

circle = Circle(4)
circle.S()
circle.P()
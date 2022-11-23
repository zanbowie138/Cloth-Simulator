import math
import numpy

from point import Point
from stick import Stick
class Cloth():
    def __init__(self, x, y, width, height, spacing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spacing = spacing

    def generate_points(self):
        self.points = numpy.empty((self.width, self.height), dtype=Point)
        for i, w in enumerate(self.points):
            for j, h in enumerate(self.points[0]):
                self.points[i][j] = Point(self.x + self.spacing * i,self.y + self.spacing * j)
                #print(self.x + self.spacing * i)

        self.sticks = numpy.empty((0), dtype=Stick)
        for x in range(self.width):
            for y in range(self.height):
                if (x+1 < self.width):
                    self.sticks = numpy.append(self.sticks, Stick(self.points[x][y], self.points[x+1][y]))
                if (y+1 < self.height):
                    self.sticks = numpy.append(self.sticks, Stick(self.points[x][y], self.points[x][y+1]))


    
        
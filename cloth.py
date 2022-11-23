import numpy as np
import math

from point import Point
from stick import Stick

class Cloth():

    def __init__(self, x, y, width, height, spacing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spacing = spacing
        self.locked = [[]]
        self.acceleration = np.array([0,0])

    def generate_points(self):
        self.pos_current = np.empty((self.width, self.height,2))
        for i, w in enumerate(self.pos_current):
            for j, h in enumerate(self.pos_current[0]):
                self.pos_current[i][j] = [self.x + self.spacing * i,self.y + self.spacing * j]
        
        self.pos_old = np.copy(self.pos_current)

    def generate_sticks(self):
        self.sticks = np.empty((0,2))
        for x in range(self.width):
            for y in range(self.height):
                if (x+1 < self.width):
                    self.sticks = np.append(self.sticks, [self.pos_current[x][y], self.pos_current[x+1][y]])
                if (y+1 < self.height):
                    self.sticks = np.append(self.sticks, [self.pos_current[x][y], self.pos_current[x][y+1]])

    def update(self, dt):
        GRAVITY = np.array([0,1000])

        self.accelerate(GRAVITY)
        self.update_pos(dt)

        self.generate_sticks()

    def update_pos(self, dt):
        velocity = np.subtract(self.pos_current, self.pos_old)

        #Save current position
        self.pos_old = self.pos_current

        #Perform Verlet Integration
        self.pos_current = self.pos_current + velocity + self.acceleration * dt * dt

        #Reset acceleration
        self.acceleration = np.array([0,0])
        

    def accelerate(self, acc):
        self.acceleration = np.add(self.acceleration, acc)



    
        
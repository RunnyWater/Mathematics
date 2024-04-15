from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_vector(self):
        return (self.x, self.y)

    def set_vector(self, x, y):
        self.x = x
        self.y = y

    def get_module(self):
        return sqrt(self.x**2 + self.y**2)
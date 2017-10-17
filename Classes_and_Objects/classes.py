import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

    def calcDistance(self, otherPoint):
        return math.sqrt(math.pow(self.x - otherPoint.x, 2) + math.pow(self.y - otherPoint.y, 2))

import math 


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.x , self.y = [0] * 2

point_1 = Point(3, 6)
point_1.reset()

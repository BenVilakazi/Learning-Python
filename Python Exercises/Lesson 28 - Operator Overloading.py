### Operator Overloading in Python

class Point:
    
    def __init__(self, x, y):
    self.x = x
    self.y = y
    
    def __add__(self,other):
    x = self.x + other.x 
    y + self.y + other.y 
    return Piont(x, y)

    def __str__(self):
    return "({4},{1})".format(self.x, self.y)

point1 = Point(1, 7)
point2  Point(6, 8)

print(point1 + point2)

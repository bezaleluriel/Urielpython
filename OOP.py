import math


class Point:
    def __init__(self, x, y):
        self.pX = x
        self.pY = y

    def __str__(self):
        return f'x={self.pX}, y={self.pY}'

    def __repr__(self):
        return f'Object: x={self.pX}, y={self.pY}'


    def __len__(self):
        return int(math.sqrt(self.pX**2 + self.pX**2))

class ColoredPoint(Point):
    def __init__(self, x, y, color):
        # take constructor features from father, like implements in c#
        super().__init__(x, y)
        self.color = color


    def __str__(self):
        return super().__str__() + f', color={self.color}'

if __name__ == '__main__':
    p3 = ColoredPoint(3, 4, 'white')
    print(p3)



    p1 = Point(3, 4)
    p2 = Point(5, 6)

    x = str(p1)
    x2 = p1.__str__()
    x3 = repr(p1)
    x4 = len(p2)
    print(x)
    print(x2)
    print(x3)
    print(x4)



    input()
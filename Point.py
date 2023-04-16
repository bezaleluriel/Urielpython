class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):


    def __gt__(self, other):
        if self.x**2 + self.y**2 > other.x**2 + other.y**2:

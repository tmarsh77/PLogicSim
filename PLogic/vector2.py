import numbers
import math

from PLogic.math import Math


class Vector2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def zero():
        return Vector2(0, 0)

    @staticmethod
    def one():
        return Vector2(1, 1)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Vector2(self.x * other, self.y * other)
        else:
            raise ArithmeticError

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return Vector2(self.x / other, self.y / other)
        else:
            raise ArithmeticError

    def __str__(self):
        return "Vector2(%f, %f)" % (self.x, self.y)

    def to_array(self):
        return [self.x, self.y]

    @staticmethod
    def lerp(a, b, t):
        x = Math.lerp(a.x, b.x, t)
        y = Math.lerp(a.y, b.y, t)
        return Vector2(x, y)

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalized(self):
        scale = 1 / self.length()
        normalized = Vector2(self.x, self.y)
        return normalized * scale

    @staticmethod
    def distance(a, b):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    @staticmethod
    def from_array(array):
        return Vector2(array[0], array[1])

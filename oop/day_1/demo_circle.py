from abc import ABC
from math import pi

from oop.day_1.demo_shape import Shape


class Circle(Shape):
    def __init__(self, r, side):
        super().__init__(side)
        self.r = r

    def cal_c(self):
        c = round(2 * pi * self.r, 2)
        return c

    def cal_s(self):
        s = round(self.r ** 2 * pi, 2)
        return s

    def __str__(self):
        return "Chu vi hinh tron: " + str(self.cal_c()) + "\nDien tich hinh tron: " + str(self.cal_s())


if __name__ == "__main__":
    circle = Circle(r=5, side=1)
    # print(circle.cal_s())
    # print(circle.cal_c())
    print(circle)
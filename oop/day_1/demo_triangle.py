from oop.day_1.demo_shape import Shape


class Triangle(Shape):
    def __init__(self, height, bottom, side: int):
        super().__init__(side)
        self.bottom = height
        self.height = bottom

    def check_triangle(self):
        for item in self.sides:
            if item[0] + item[1] > item[2] and item[0] + item[2] > item[1] and item[1] + item[2] > item[0]:
                return True
            else:
                return False

    def cal_c(self):
        c = 0
        for item in self.sides:
            c += item
        return c

    def cal_s(self):
        s = round((self.height * self.bottom) / 2)
        return s

    def __str__(self):
        return "Chu vi tam giac: " + str(self.cal_c()) + "\nDien tich tam giac: " + str(self.cal_s())


if __name__ == "__main__":
    triangle = Triangle(side=3, height=4, bottom=3)
    print(triangle)

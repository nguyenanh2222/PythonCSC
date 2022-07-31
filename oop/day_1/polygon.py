import math


class Polygon():
    def __init__(self, number_of_sides):
        """Contructor"""
        self.number_of_side = number_of_sides
        self.sides = []

    def input_sides(self):
        self.sides = [int(input("INPUT SIDE: ") + str(i))
                      for i in range(self.number_of_side)]

    def output_sides(self):
        for i in range(self.number_of_side):
            print('SLIDES' + str(i + 1) + ': ' + str(self.sides[i]))


class Triangle(Polygon):
    """docclass: Description class attribute"""

    def __init__(self):
        super().__init__(3)

    def cal_circumference(self):

        # circumference (self.sides)

        return circumference

    def cal_area(self):
        p = self.cal_circumference() / 2
        a, b, c = self.number_of_side
        heron_p = p * (p - a) * (p - b) * (p - c)
        s = math.sqrt(heron_p)
        return s

    def display(self):
        print('Circumference Triangle: ', round(self.cal_circumference(), 2))
        print('Area Triangle', round(self.cal_area(), 2))


if __name__ == "__main__":
    triangle = Triangle()
    print(triangle.input_sides())
    print(triangle.cal_circumference())

import math


class Triangle:
    """docclass: Description class attribute"""

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def cal_circumference(self):
        circumference = self.a + self.b + self.c
        return circumference

    def cal_area(self):
        p = self.cal_circumference() / 2
        heron_p = p * (p - self.a) * (p - self.b) * (p - self.c)
        s = math.sqrt(heron_p)
        return s

    def display(self):
        print('Circumference Triangle: ', round(self.cal_circumference(), 2))
        print('Area Triangle', round(self.cal_area(), 2))

    def __str__(self):
        """khong dung print , ham __str__ chi return object kieu string"""
        result = f'Circumference {round(self.cal_circumference(), 2)} \n'
        result += f'Area {round(self.cal_area(), 2)}'
        return result

    def __del__(self):
        pass


if __name__ == "__main__":
    a = float(input('input a: '))
    c = float(input('input c: '))
    b = float(input('input b: '))
    triangle = Triangle(a=4,
                        b=5,
                        c=6)
    if a + b > c and a + c > b and b + c > a:
        print(triangle.display())
        setattr(triangle, 'a', 10)
        print(getattr(triangle, 'a'))
        print(hasattr(triangle, 'f'))
        print(delattr(triangle, 'a'))
        print(triangle.display())
        print(triangle.__doc__)
        print(triangle.__dict__)
        # print(triangle.__name__) -> 3.6 cho ra ten class

        print(triangle.__class__)
        print(triangle.__module__)

    triangle.__del__()

    # else:
    #     print("Error Triangle")

# bug: Traceback(most
#     recent
#     call
#     last):
#     File
#     "C:/Users/hv/Desktop/respository/demo_triange.py", line
#     37, in < module >
#     a = float(input('input a: '))
# ValueError: could
# not convert
# string
# to
# float: ''



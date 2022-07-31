from abc import abstractmethod, ABC
from typing import Union


class Shape(ABC):
    def __init__(self, side: int):
        self.side = side
        self.sides = [int(input("nhap do dai canh: ")) for item in range(side)]

    def __str__(self):
        return "Shape has: " + str(self.side) + " side"

    @abstractmethod
    def cal_c(self):
        ...

    def cal_s(self):
        ...


if __name__ == "__main__":
    shape = Shape(5)
    print(shape)

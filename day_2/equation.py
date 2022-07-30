class Equation():
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


    def find_x(self):
        if self.a == 0 and self.b == 0:
            return {'messenger': 'Wealth of counter'}
        elif self.a == 0 and self.b != 0:
            return {'messenger': 'Its not equation'}
        else:
            x = -self.b / self.a
            if x:
                return {'messenge': f"x = {round(x, 2)}"}
            else:
                return None


if __name__ == '__main__':
    q = 0
    while q == 0:
        a = int(input("Input a: "))
        b = int(input("Input b: "))
        equation = Equation(a=a, b=b)
        print(equation.find_x())
        q = int(input('Do you want continue ? (0: continue) (1: break) '))
        if q != 1:
            break

# from abc import ABC, abstractmethod
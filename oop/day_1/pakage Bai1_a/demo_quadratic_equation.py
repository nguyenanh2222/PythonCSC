class QuandraticEquation():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        if self.a == 0:
            return "Phương trình vô nghiệm"
        if self.a == 0 and self.b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Nghiệm của phương trình: " + str(self.find_x())
    def find_x(self):
        x = -self.b/self.a
        return x
if __name__=="__main__":
    quadratic_equation = QuandraticEquation(a=1, b=2)
    print(quadratic_equation)
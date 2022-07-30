class Vector():
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    def __str__(self):
        return f"""So nguyen a: {self.a} - So nguyen b: {self.b}"""
    def __add__(self, orther):
        return Vector(self.a + orther.a, self.b + orther.b)

if __name__== "__main__":
    vector_1 = Vector(1, 2)
    vector_2 = Vector(3, 4)
    print(vector_1)
    print(vector_2)
    vector_3 = vector_1 + vector_2
    print(vector_3)

    # public
    # protected
    # private
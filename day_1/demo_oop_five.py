from datetime import date
from decimal import Decimal


class Person():
    def __init__(self, name: str, birth: str, place_of_birth, gender):
        self.name = name
        self.birth = birth
        self.place_of_birth = place_of_birth
        self.gender = gender

    def __str__(self):
        str_information = 'Name' + self.name
        str_information += '\nBirth ' + self.birth
        str_information += '\nPlace Of Birth ' + self.place_of_birth
        str_information += '\nGender ' + self.gender
        return str_information


class Children(Person):
    def __init__(self, name: str, birth: str, place_of_birth: str, gender: str, mssv: str, luong: Decimal):
        super().__init__(name, birth, place_of_birth, gender)
        self.mssv = mssv
        self.luong = luong

    # def __str__(self):
    #     str_information = super().__str__()
    #     str_information += '\nID ' + self.mssv
    #     str_information += '\nSalary ' + '{:,}'.format(self.luong)
    #     return str_information

    # khoi tao


person = Person('Nguyen Van A', "11/11/91", 'tpHCM', 'Nam')
child = Children('Tran Thi C', "22/12/1992", 'Tien Giang', 'Nu', 'NV01', Decimal(15000000.0))
print(child)
# ghi de phuong thuc -> dinh nghia lai tren ham da co
print("==========================")
print(issubclass(Children, Person))
print("++++++++++++++++++++++++++")
print(isinstance(child, Person))
print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(isinstance(person, Children))

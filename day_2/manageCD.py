from decimal import Decimal
from unicodedata import decimal

class CD():
    def __init__(self,
                 name_cd: str,
                 singer_name: str,
                 songs: int,
                 cost: float):
        self.name_cd = name_cd
        self.singer_name = singer_name
        self.songs = songs
        self.cost = cost
        self.total_amount = self.cost*self.songs

    def __str__(self):
        return f"{self.name_cd}-{self.singer_name}- {self.songs} - {self.cost}"

    def calcualate(self):
        total_amount = 0
        total_amount += self.total_amount
        return total_amount

if __name__ == '__main__':
    q = 1
    while q == 1:
        print('--- Danh sach CD: --- ')
        name_cd = input('Nhap ten CD: ')
        singer_name = input(('Nhap ten ca sy: '))
        songs = int(input('Nhap so bai hat: '))
        cost = float(input('Nhap gia thanh: '))
        cd = CD(name_cd=name_cd,
                singer_name=singer_name,
                songs=songs,
                cost=cost)
        q = int(input("continue (1) or stop (0)"))
        if q == 0:
            break


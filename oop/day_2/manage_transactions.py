import datetime
from decimal import Decimal


class GiaoDich():
    def __init__(self,
                 loai: str,
                 ma_gd: str,
                 ngay_gd: str,
                 so_luong: int,
                 don_gia: Decimal):
        self.ma_gd = ma_gd
        self.ngay_gd = datetime.datetime.strptime(ngay_gd, '%Y/%m/%d')
        self.so_luong =
        self.loai = loai
        self.don_gia = don_gia
        self.thanh_tien = self.don_gia * self.so_luong



    def __str__(self):
        _str = " - "
        return self.ma_gd + _str +str(self.ngay_gd) + _str  + str(self.loai) + _str + str(self.so_luong) + _str + str(self.don_gia) + str(self.thanh_tien)

class GiaoDichTienTe(GiaoDich):
    def __init__(self,
                 loai: str,
                 ma_gd: str,
                 ngay_gd: str,
                 so_luong: int,
                 don_gia: Decimal):
        super().__init__(loai, ma_gd, ngay_gd, so_luong, don_gia)
        self.thanh_tien = self.don_gia * self.so_luong
        self.loai = str

if __name__ == '__main__':
    q = int(input())
    while q == 1:
        print("""Quan ly giao dich \n""")
        ma_gd = input("Nhap ma giao dich: ")
        ngay_gd = input("Nhap ngay giao dich: ")
        so_luong = int(input("Nhap so luong: "))
        loai_giao_dich = int(input("Chon loai giao dich: 1: Vang, 2: Tien te: "))
        if loai_giao_dich == 1:
            loai = input("Chon loai 18k/ 24k/ 9999: ")
            don_gia = Decimal(input("Nhap don gia: "))
            giao_dich_vang= GiaoDich(ma_gd=ma_gd,
                                ngay_gd=ngay_gd,
                                so_luong=so_luong,
                                loai=loai,
                                don_gia=don_gia)
            list_giao_dich_vang = []
            list_giao_dich_vang.append(giao_dich_vang)
            tong_loai_giao_dich = 0
            tong_thanh_tien_giao_dich = 0
            for giao_dich in list_giao_dich_vang:
                tong_loai_giao_dich += giao_dich.loai
                tong_thanh_tien_giao_dich += giao_dich.thanh_tien
            print("Tong so luong: ", tong_loai_giao_dich)
            print(("Tong so tien: ", tong_thanh_tien_giao_dich))
            q = int(input("Ban co muon tiep tuc khong? 1: Co, 2: Khong: "))

        elif loai_giao_dich == 2:
            loai = input("Chon loai USD/ EUR/ AUD: ")
            don_gia = Decimal(input("Nhap ty gia: "))
            giao_dich_tien= GiaoDich(ma_gd=ma_gd,
                                ngay_gd=ngay_gd,
                                so_luong=so_luong,
                                loai=loai,
                                don_gia=don_gia)
            list_giao_dich_tien = []
            list_giao_dich_tien.append(giao_dich_tien)
            tong_loai_giao_dich = 0
            tong_thanh_tien_giao_dich = 0
            for giao_dich in list_giao_dich_tien:
                tong_loai_giao_dich += giao_dich.loai
                kieu_giao_dich = int(input("Ban chon mua hay ban: (1: Co), (0: khong)"))
                if kieu_giao_dich == 1:
                    ...
                elif kieu_giao_dich == 0:
                    ...
                tong_thanh_tien_giao_dich += giao_dich.thanh_tien

            print("Tong so luong: ", tong_loai_giao_dich)
            print(("Tong so tien: ", tong_thanh_tien_giao_dich))











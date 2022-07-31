ten_hang = 'Honda'
# => roi rac

class XeOto():
    """"classdoc"""
    """attribute"""
    def __init__(self,
                 ten_hang: str = None,
                 mau_sac: str = None,
                 so_cho_ngoi: int = None):
        """khong co gia tri return -> khong dung return o cuoi
        tat ca cac thuoc tinh deu la bien toan cuc
        * Gan thuoc tinh ngay khi khoi tao"""
        self.ten_hang = ten_hang
        self.mau_sac = mau_sac
        self.so_cho_ngoi = so_cho_ngoi
    """method"""
    def in_thong_tin(self):
        print('ten hang', self.ten_hang)
        print('mau sac', self.mau_sac)
        print('so cho ngoi', self.so_cho_ngoi)

"""=== khoio tao doi tuong ==="""

if __name__ == '__main__':
    xe1 = XeOto(ten_hang='Honda',
                mau_sac='Den',
                so_cho_ngoi=5)
    xe1.in_thong_tin()
    print("-------------")
    xe2 = XeOto()
    xe2.mau_sac = 'DEN'
    xe_mau_capitalize =  xe2.mau_sac.capitalize()
    print("--------------")
    print(xe_mau_capitalize)
    print("--------------")
    xe2.ten_hang = 'Toyota'
    xe2.so_cho_ngoi = 4
    xe2.in_thong_tin()

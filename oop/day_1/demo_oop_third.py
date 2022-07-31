ten_hang = 'Honda'
# => roi rac

class XeOto():
    """"classdoc"""
    """attribute"""
    ten_hang = 'Toyota'
    mau_sac = 'Do'
    so_cho_ngoi = 5

    """method"""
    def in_thong_tin(self):
        print('ten hang', self.ten_hang)
        print('mau sac', self.mau_sac)
        print('so cho ngoi', self.so_cho_ngoi)

"""=== khoio tao doi tuong ==="""

if __name__ == '__main__':
    xe1 = XeOto()
    xe1.in_thong_tin()
    print("-------------")
    xe2 = XeOto()
    xe2.mau_sac = 'trang'
    xe2.in_thong_tin()
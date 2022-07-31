import xml.dom.minidom
from class_don_vi import DonVi, NhanVien


def tao_danh_sach_don_vi(list_don_vi):
    DOMTree = xml.dom.minidom.parse("../files_xml/don_vi.xml")
    collection = DOMTree.documentElement
    don_vi_s = collection.getElementsByTagName("DON_VI")
    for don_vi in don_vi_s:
        if don_vi.hasAttribute("ID") and don_vi.hasAttribute("Ten"):
            dv = DonVi(don_vi.getAttribute("ID"), don_vi.getAttribute("Ten"))
            list_don_vi.append(dv)
    return


def tao_danh_sach_nhan_vien(list_nhan_vien):
    DOMTree = xml.dom.minidom.parse("../files_xml/nhan_vien.xml")
    collection = DOMTree.documentElement
    nhan_vien_s = collection.getElementsByTagName("NHAN_VIEN")
    for nhan_vien in nhan_vien_s:
        if nhan_vien.hasAttribute("ID") and nhan_vien.hasAttribute("ID_DON_VI"):
            nv = NhanVien(nhan_vien.getAttribute("ID"),
                          nhan_vien.getAttribute("Ho_ten"),
                          nhan_vien.getAttribute("Gioi_tinh"),
                          nhan_vien.getAttribute("Ngay_sinh"),
                          nhan_vien.getAttribute("CMND"),
                          nhan_vien.getAttribute("Muc_luong"),
                          nhan_vien.getAttribute("Dia_chi"),
                          nhan_vien.getAttribute("ID_DON_VI"))
            list_nhan_vien.append(nv)
    return


def thong_ke_don_vi(iddv, list_nhan_vien):
    count = 0
    so_nam = 0
    so_nu = 0
    for nv in list_nhan_vien:
        if int(nv.id_don_vi) == iddv:
            print(nv.id_don_vi, "-", nv.ho_ten, "-", nv.cmnd)
            count += 1
            if nv.gioi_tinh == 'true':
                so_nam += 1
            else:
                so_nu += 1
    print("Tong so nhan vien", count, "- Trong do co: ", so_nam, "nam, va ", so_nu, "nu")


def tim_kiem_nhan_vien(ten, list_nhan_vien):
    count = 0
    nv_s = []
    for nv in list_nhan_vien:
        try:
            if nv.ho_ten.lower().find(ten.lower()) != -1:
                count += 1
                nv_s.append(nv.ho_ten)
        except:
            return
    return nv_s


if __name__ == "__main__":
    list_don_vi = []
    tao_danh_sach_don_vi(list_don_vi)
    list_nhan_vien = []
    tao_danh_sach_nhan_vien(list_nhan_vien)
    iddv = int(input("ban muon xem thong tin don vi (nhap so): \t"))
    print("Ket qua thong ke")
    print(tim_kiem_nhan_vien('phí', list_nhan_vien))

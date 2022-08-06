from repo import ProductRepo


class Interface():
    def show(self):
        while True:
            print("""
            1: Hien thi danh sach san pham \n
            2: Them san pham \n
            3: Tim kiem san pham \n
            4: Cap nhat danh sach san pham \n
            5: Xoa danh sach san pham
            """)
            choose = input("Chon chuc nang: ")
            if choose == "1":
                products = ProductRepo().get_products_repo()
            elif choose == "2":
                name = input('Name: ')
                price = input('Price: ')
                amount = input('Amount: ')
                product = ProductRepo().insert_product(name=name, price=price, amount=amount)
            elif choose == "3":
                products = ProductRepo().search_product()
            elif choose == "4":
                product = ProductRepo().update_product()
            elif choose == "5":
                product = ProductRepo().delete_product()
            choose = input("Ban co muon TT (1 Co) (0 Khong) ")
            if choose == "0":
                break




if __name__ == "__main__":
    interface = Interface()
    interface.show()

import sqlite3
cnn = sqlite3.connect("../db/product.db")
class ProductRepo:
    def get_products_repo(self):
        sql = """
        SELECT *
        FROM product"""
        curses = cnn.execute(sql)
        for product in curses:
            print(product[0])
        return curses
    def insert_product(self, name, price, amount):
        sql = f"""
        INSERT INTO product (
        name, price, amount)
        VALUES (
        ?,?,?         
        )
        """
        cursor = cnn.execute(sql, (name, price, amount))
        cnn.commit()
        if cursor.rowcount > 0:
            print("Them thanh cong")
        else:
            print("Them khong thanh cong")

    def search_product(self, name, price, amount):
        sql = f"""
        SELECT * 
        FROM product
        WHERE name LIKE '%{name}%' 
        OR price = {price}
        OR amount = {amount} 
        """
        cursor = cnn.execute(sql, (name, price, amount))
        return cursor

    def update_product(self):
        ...

    def delete_product(self):
        ...

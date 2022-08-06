import sqlite3

cnn = sqlite3.connect("../db/product.db")

sql = """
CREATE TABLE product(
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
price REAL NOT NULL,
amount INTEGER NOT NULL
)
"""

cnn.execute(sql)

import sqlite3
cnn = sqlite3.connect('db/qlvattu.db')
chuoiSQLPhong =  """
Create table Phong
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten text not null Unique,
    chuc_nang text not null
)
"""
cnn.execute(chuoiSQLPhong)

chuoiSQLNhanVien = """
Create table NhanVien(
    id int primary key,
    hoTen text not null Unique,
    tuoi int,
    diaChi text not null,
    luong real,
    phong_id int not null,
    foreign key(phong_id) references Phong(id)
    )"""
cnn.execute(chuoiSQLNhanVien)
cnn.close()
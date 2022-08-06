import sqlite3
cnn = sqlite3.connect('db/qlvattu.db')
# chuoisql = """
# insert into Phong(ten, chuc_nang)
# values('GD', 'Phong lam viec GD')
# """

chuoisql = """
update Phong 
set chuc_nang = 'Phong lam viec TP'
where id = 1

"""
curses = cnn.execute(chuoisql)
cnn.commit()
if curses.rowcount > 0:
    print("Successfully")
else:
    print("UnSuccessfully")
cnn.close()
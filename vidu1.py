import sqlite3
conn = sqlite3.connect('bd/qlvattu.db')
chuoiSQL = '''
create table Company(
Id Int primary key not null,
Name Text not null
Age int not null
Address VarChar
)

'''
import sqlite3
cnn = sqlite3.connect('db/qlvattu.db')
chuoiSQL = '''
create table Company(
Id Int primary key not null,
Name Text not null,
Age int not null,
Address VarChar (150),
Salary real
);
'''
cnn.execute(chuoiSQL)
print("Successfully")
cnn.close()
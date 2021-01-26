import sqlite3
db1=sqlite3.connect("news.db")
db1.execute('''create table akshay15(s_id varchar);''')
x=db1.execute('select * from akshay15;')
print(x)
db1.close()

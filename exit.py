import sqlite3 as s
conn=s.connect("db1.db")
conn.execute('''create table new(s_id text(10);''')
conn.execute("insert into new values('23')")
conn.close()

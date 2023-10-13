from sqlite3 import *

con = connect("data.db")
cur = con.cursor()

a = [("primon", "123")]
cur.excecute("create table users (login text, pwd text)")

cur.excecute("insert into users values (?,?)", a)
con.commit()

for i in cur.excecute("select * from users"):
  print(i)

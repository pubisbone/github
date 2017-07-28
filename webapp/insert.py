import MySQLdb

db = MySQLdb.connect("localhost","root","1234","SCOTT")
cur = db.cursor()
sql = "delete from EMP where empno = 7777"
try:
    cur.execute(sql)
    db.commit()
 
except:
    db.rollback()

cur.execute("select * from EMP")
rs = cur.fetchall()
for i in rs:
      print(i)
cur.close()
db.close()


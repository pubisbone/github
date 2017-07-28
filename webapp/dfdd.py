import MySQLdb
from flask import Flask
from flask import render_template
from flask import request



db=MySQLdb.connect("localhost","root","1234","idpw")
cur = db.cursor()
cur.execute("select pw from namedata where id='a'")
result=cur.fetchone()
print(result)
 
cur.close()
db.close()

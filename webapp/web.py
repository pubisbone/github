# coding : utf-8
import MySQLdb
from flask import Flask
from flask import render_template
from flask import request
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.LOW)
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
@app.route('/shutdown') #http://192.168.1.169:8887/shutdown
def shutdown():
    shutdown_server()
    return 'Server shutting down..'


@app.route('/insert')
def insert():
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    try:
        cur.execute("insert into EMP(empno,ename) values(123,'dsf')")
        db.commit()
        return 'oo'
    except:
        db.rollback()
        return 'xx'
    
    
    cur.close()
    db.close()

@app.route('/delete')
def delete():
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    try:
        cur.execute("delete from EMP where empno = 777")
        db.commit()
        return 'oo'
    except:
        db.rollback()
        return 'xx'
    
    
    cur.close()
    db.close()

@app.route('/create')
def create():
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    try:
        cur.execute("create table BAAANG(name varchar(20))")
        #cur.execute("insert into BAANG(name) value('sdf')")
        db.commit()
        return 'oo'
    except:
        db.rollback()
        return 'xx'
    cur.close()
    db.close()
    
@app.route('/') #http://192.168.1.169:8887
def hello():
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    cur.execute("select empno,ename from EMP")
    row = cur.fetchall()
    Data = {'data' : row}   #2 arr
    return render_template('test2.html', **Data)
    cur.close()
    db.close()


@app.route('/select/<int:x>')
def number(x):
    db = MySQLdb.connect("localhost","root","1234","SCOTT")
    cur = db.cursor()
    cur.execute("select * from EMP where empno=%d" %x)
    result = cur.fetchall()
    Data = {'data' : result}
    return render_template('test3.html', **Data)
    cur.close()
    db.close()

@app.route('/led/<a>')
def led(a):

    if a=="on":
        GPIO.output(24, GPIO.HIGH)
        return 'fuck'
    if a=="off":
        GPIO.output(24, GPIO.LOW)
        return 'shit'
  
        
    
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8887, debug=True)
    
  
       

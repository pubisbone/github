# coding : utf-8
import Adafruit_DHT
import time
import Adafruit_DHT
import time
import datetime
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

    
@app.route('/') #http://192.168.1.169:8887
def hello():
    db = MySQLdb.connect("localhost","root","1234","DHT11")
    cur = db.cursor()
    cur.execute("select * from hutemp")
    row = cur.fetchall()
    Data = {'data' : row}   #2 arr
    return render_template('new.html', **Data)
    cur.close()
    db.close()


@app.route('/<x>')
def number(x):
    db = MySQLdb.connect("localhost","root","1234","DHT11")
    cur = db.cursor()
    cur.execute("select * from hutemp where t_min=%s" %x)
    result = cur.fetchall()
    Data = {'data' : result}
    return render_template('new.html', **Data)
    cur.close()
    db.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8887, debug=True)
    





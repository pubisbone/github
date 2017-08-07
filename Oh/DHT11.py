import MySQLdb
import Adafruit_DHT
import time   #delay
import datetime   #time pasing
from flask import Flask
from flask import render_template
from flask import request
import RPi.GPIO as GPIO



    
sensor = Adafruit_DHT.DHT11
pin = 24   #GPIO
db = MySQLdb.connect("localhost","root","1234","DHT11")
while True:
    wtime = datetime.datetime.now()
    
    t_year = wtime.strftime('%Y')
    t_month = wtime.strftime('%m')
    t_day = wtime.strftime('%d')
    t_hour = wtime.strftime('%H')
    t_min = wtime.strftime('%M')

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    cur = db.cursor()
    try:
        cur.execute("insert into hutemp values(%s, %s, %s, %s, %s, %s, %s)" %(t_year, t_month, t_day, t_hour, t_min, humidity, temperature))
        db.commit()
    except:
        db.rollback()
        print("ddd")
    
    cur.close()
    time.sleep(60)


    
    

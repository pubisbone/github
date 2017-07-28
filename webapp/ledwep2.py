from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO


app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
@app.route("/LED/ON")
def ledon():
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, GPIO.HIGH)
    return 'led test'
@app.route("/")
def index():
    return render_template("selected.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8886,debug=True)
    
    

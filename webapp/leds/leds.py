from flask import Flask
from flask import render_template
from flask import request
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)

leds = {
    24 : {'name' : 'LED', 'state' : GPIO.LOW}
}

for led in leds:        #24port init
    GPIO.setup(led, GPIO.OUT)   #led=24, output state
    GPIO.output(led, GPIO.LOW)  #led=24, LOW

def getGpioState():      #status confirm
    for led in leds:
        leds[led]['state'] = GPIO.input(led)    #state of 24's state
    return leds

@app.route("/")
def main():
    gpioState = {
        'leds' : getGpioState()
    }
    return render_template('main.html', **gpioState)

@app.route("/<led>/<act>")
def action(led, act):
    led = int(led)
    leds = getGpioState()
    dev = leds[led]['name']     #LED

    if act == "on":
        GPIO.output(led, GPIO.HIGH)
        msg = "Turned" + dev + "on."
    elif act == "off":
        GPIO.output(led, GPIO.LOW)
        msg = "Turned" + dev + "off."
    else:
        msg = "Undefined action!"

    gpioState = {
        'msg' : msg,
        'leds' : getGpioState()
    }

    return render_template('main.html', **gpioState)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888,debug=True)

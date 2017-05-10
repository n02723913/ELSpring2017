import RPi.GPIO as GPIO
from flask import Flask, render_template, request, redirect, url_for
import time
#from SimpleCV import Camera
#sudo apt-get install python-opencv
from picamera import PiCamera
from time import sleep

#camera = PiCamera()

#camera.start_preview()
#sleep(10)
#camera.stop_preview()

app = Flask(__name__)

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(0, GPIO.OUT)  
#pwm1 = GPIO.PWM(0, 50)  
#pwm1.start(5)  
#GPIO.setup(1, GPIO.OUT)  
#pwm2 = GPIO.PWM(1, 50)  
#pwm2.start(7.5)  


@app.route("/")
def main():
    templateData={
        'x' : 0 ,
        'y' : 0,
        'deg': 10,
        }
    return render_template('index.html', **templateData)
    


@app.route("/move", methods = ['POST', 'GET'])
def move():
    x=request.form('x')
    dx2=1./18.*(x)+2
    pwm1.ChangeDutyCycle(dx2)
    time.sleep(1)
    y=request.form('y')
    return render_template('index.html')

@app.route("/reset")
def reset():
    dx2=1./18.*(0)+2
    pwm1.ChangeDutyCycle(dx2)    
    time.sleep(1)
    return render_template('index.html')


@app.route("/capture", methods = ['POST', 'GET'])
def capture():

  	
    camera = PiCamera()
    camera.start_preview()
    sleep(5)
    camera.capture('/home/pi/Desktop/img/i.jpg')
    camera.stop_preview()
    return render_template('index.html')
   
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

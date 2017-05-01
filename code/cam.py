import RPi.GPIO as GPIO
from flask import Flask, render_template, request
import time
from SimpleCV import Camera
#sudo apt-get install python-opencv


app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(0, GPIO.OUT)  
pwm1 = GPIO.PWM(0, 50)  
pwm1.start(5)  
GPIO.setup(1, GPIO.OUT)  
pwm2 = GPIO.PWM(1, 50)  
pwm2.start(7.5)  


@app.route("/")
def main():
   x  = 0
   y =0
   deg= 10
   dx=0
   dy=0

   return render_template('index.php', **templateData)

    
# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/1/<action>")
def action(action):
  
    pwm1.ChangeDutyCycle(7.5)  # turn towards 90 degree #Open   
    time.sleep(1)  

    if action == "left":
          x=x-deg
          dx=1./18.*(x)+2
          pwm1.ChangeDutyCycle(dx)  # turn towards 90 degree #Open   
          time.sleep(1)  
    if action == "right":
          x=x+deg
          dx=1./18.*(x)+2
          pwm1.ChangeDutyCycle(7.5)  # turn towards 90 degree #Open
          time.sleep(1)  
    if action == "down":
          y=y-deg
          dy=1./18.*(y)+2
          pwm2.ChangeDutyCycle(7.5)  # turn towards 90 degree #Open
          time.sleep(1)  
    if action == "up":
          y=y+deg
          dy=1./18.*(y)+2
          pwm2.ChangeDutyCycle(7.5)  # turn towards 90 degree #Open
          time.sleep(1)  
    if action == "reset":
          pwm2.ChangeDutyCycle(0)  # turn towards 90 degree #Open
          time.sleep(1)  
          pwm1.ChangeDutyCycle(0)  # turn towards 90 degree #Open   
          time.sleep(1)
          x=0
          y=0  
       
    # For each pin, read the pin state and store it in the pins dictionary:
    
    x = GPIO.input(pin);
    y = GPIO.input(pin);
    return render_template('index.php', **templateData)@app.route("/cap/<action>")
def action(action):
    if action == "takepic":
       
cam = Camera()
time.sleep(0.1)  # If you don't wait, the image will be dark
img = cam.getImage()
img.save("simplecv.png")
    return render_template('index.php', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
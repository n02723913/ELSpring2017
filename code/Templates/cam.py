from __future__ import division 
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import time
#from SimpleCV import Camera sudo apt-get install python-opencv
from picamera import PiCamera
# Author: Tony DiCola License: Public Domain
import time
import os
# Import the PCA9685 module.
import Adafruit_PCA9685
# Uncomment to enable debug output. import logging 
#logging.basicConfig(level=logging.DEBUG)
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
# Alternatively specify a different address and/or bus: pwm = 
#Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)
# Configure min and max servo pulse lengths
servo_min = 150 # Min pulse length out of 4096 
servo_max = 600 # Max pulse length out of 4096 
i=1
#camera.start_preview() sleep(10) camera.stop_preview()
app = Flask(__name__, template_folder='../Templates')
#GPIO.setmode(GPIO.BOARD) GPIO.setup(0, GPIO.OUT) pwm1 = GPIO.PWM(0, 50) 
#pwm1.start(5) GPIO.setup(1, GPIO.OUT) pwm2 = GPIO.PWM(1, 50) 
#pwm2.start(7.5)
def main(agrv):
    global x
    global y
    x=0
    y=0
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 
@app.route("/") 
def start():
    global x
    x= 0
    global y
    y=0
    templateData={
       'x' : x ,
       'y' : y,
       'deg': 10
    }
    return render_template('index.html',**templateData)
@app.route("/move", methods = ['POST', 'GET'])
def pulserrrrr():
    global x,y
    #set_servo_pulse(0,0,0,0)
    dx = request.form.get('x')
    dy= request.form.get('y')
    dx = int(dx)
    dy = int(dy)
    set_servo_pulse(0,dx,2,dy,x,y)
    y=dy
    x=dy
    templateData={
    'x': dx ,
    'y': dy
	}
    return render_template('index.html', **templateData)
    # Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse, channel2, pulse2,x,y):    
    #x==request.form.get('x') dx2=1./18.*(x)+2 pwm1.ChangeDutyCycle(dx2) 
    #time.sleep(1) y==request.form.get('y')
    pulse_length = 1000000
    pulse_length //= 60
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096 # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
   # pulse *= 1000
   # pulse //= pulse_length
    pulse2_length = 1000000
    pulse2_length //=60
    print('{0}us per period'.format(pulse2_length))
    pulse2_length //= 4096 # 12 bits of resolution
    print('{0}us per bit'.format(pulse2_length))
    #pulse2 *= 1000
    #pulse2 //= pulse2_length
    pulse= x-pulse
    pulse2 = y-pulse2
    print(x)
    move= 150
    move2= 150
    if(pulse<0):
        move =600
        pulse=-(pulse)
    if(pulse2<0):
        move2= 600
        pulse2=-(pulse2)
    print(pulse)
    print(pulse2)
    x= pulse
    y= pulse2
    pwm.set_pwm(channel, 0,move )
    time.sleep(pulse*.0017)
    pwm.set_pwm(channel,0,0)
    time.sleep(1)
    pwm.set_pwm(channel2, 2, move2)
    print(pulse2)
    time.sleep(pulse2*.0017)
    pwm.set_pwm(channel2,0,0)
    time.sleep(1)
    # Set frequency to 60hz, good for servos.
    pwm.set_pwm_freq(60)
    
    print('Moving serv150on channel 0, press Ctrl-C to quit...')
    ## Move servo on channel O 2  between extremes
    servo_middle_position= (servo_max - servo_min)/2
    #try:
	   
        #pwm.set_pwm(0, 0, 600)
   	#time.sleep(.1)
        #pwm.set_pwm(0, 0, 0)
   	#time.sleep(1)
    	#pwm.set_pwm(2, 0, 150)
   	#time.sleep(.1)
        #pwm.set_pwm(2, 2, 0)
        #time.sleep(1)
   # pwm.set_pwm(0, 0, 100)
   # time.sleep(1)
   # pwm.set_pwm(2, 2, 200)
   # time.sleep(1)
    #except KeyboardInterrupt:
	#pwm.set_pwm(0,0,servo_middle_position)
	#pwm.set_pwm(2,2,servo_middle_position)
    return render_template('index.html')
@app.route("/reset") 
def reset():
    dx2=1./18.*(0)+2
    pwm1.ChangeDutyCycle(dx2)
    time.sleep(1)
    return render_template('index.html')
@app.route("/capture", methods= ['POST','GET']) 
def cap():
    if (i==1):
	camera = PiCamera()
        camera.start_preview()
    capture(camera)
    templateData={'x':x,
'y':y
}
    return render_template('index.html',**templateData) 
def capture(camera):
    i=0
    #camera = PiCamera() camera.start_preview()
    time.sleep(2)
    name = request.form.get('name')
    name = str(name)
    camera.capture('/home/pi/ELSpring2017/code/Templates/img/'+name+'i.jpg')
    camera.close()
    return render_template('index.html')
   
@app.route("/preview")
def preview():
    camera= PiCamera()
    time.sleep(2)
    camera.capture('/home/pi/ELSpring2017/code/Templates/img/preview.jpg')
    camera.close()
    return render_template('index.html') 
#TEST CODE FOR THE GALLERY 
#https://github.com/ibininja/upload_file_python
@app.route("/upload", methods=["POST"]) 
def upload():
    target = os.path.join(APP_ROOT, 'img/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)
    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("index.html", image_name=filename)#might be to a diffeent html 
@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("img", filename) 
@app.route('/gallery') 
def get_gallery():
    image_names = os.listdir('./img')
    print(image_names)
    return render_template("index.html", image_names=image_names)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)


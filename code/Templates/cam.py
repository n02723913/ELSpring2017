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

#TEST CODE FOR THE GALLERY https://github.com/ibininja/upload_file_python
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
    return render_template("index.html", image_name=filename)#might be  to a diffeent html 

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

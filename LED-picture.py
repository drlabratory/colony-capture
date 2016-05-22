import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

camera = PiCamera()
camera.resolution = (3264, 2448)

def picture_capture(filename):
    GPIO.output(18,GPIO.HIGH) # turn on LED lights
    camera.start_preview()
    sleep(5) # camera needs a few seconds to adjust levels
    camera.capture(filename) # capture image to filename
    camera.stop_preview()
    GPIO.output(18,GPIO.LOW) # turn off LED lights
    return True

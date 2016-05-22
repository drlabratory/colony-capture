import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

camera = PiCamera()
camera.resolution = (3264, 2448)

def picture_capture(filename):
    GPIO.output(18,GPIO.HIGH)
    camera.start_preview()
    sleep(5)
    camera.capture(filename)
    camera.stop_preview()
    GPIO.output(18,GPIO.LOW)
    return True

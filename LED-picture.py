import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
from sys import argv

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

camera = PiCamera()
camera.resolution = (3264, 2448)

filename = argv[1]

print "LED on"
GPIO.output(18,GPIO.HIGH)

camera.start_preview()
sleep(5)

print "Capturing Image"
camera.capture(filename)
camera.stop_preview()

print "LED off"
GPIO.output(18,GPIO.LOW)


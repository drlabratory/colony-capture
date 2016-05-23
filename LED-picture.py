import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

camera = PiCamera()
camera.resolution = (3264, 2448)

def picture_capture(filename):
    GPIO.output(18,GPIO.HIGH) # turn on LED lights
    camera.start_preview()
    sleep(5) # camera needs a few seconds to adjust levels
    camera.annotate_text = time.strftime("%c")
    camera.capture(filename) # capture image to filename
    camera.stop_preview()
    GPIO.output(18,GPIO.LOW) # turn off LED lights
    return True

counter = 1
base_name = "test_growth"
days = 1
min_interval = 20

# take a picture every [min_interval] minutes for [days] days
total_number_pictures = days*24*60 / min_interval

while counter < total_number_pictures:
    file_name = "base_name_%04d.jpg" % (base_name, counter)
    picture_capture(file_name)
    sleep_interval = min_interval*60-5
    sleep(sleep_interval)
    counter = counter + 1

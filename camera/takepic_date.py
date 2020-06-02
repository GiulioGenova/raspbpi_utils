from time import sleep
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
# Camera warm-up time

sleep(2)
date = "{:%Y%m%d%H%M}".format(datetime.now())
filename = date+'.jpg'
camera.capture(filename)

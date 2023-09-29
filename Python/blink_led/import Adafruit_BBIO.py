import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("USR3",GPIO.OUT)

GPIO.output("USR3",GPIO.HIGH)
time.sleep(0.2)
GPIO.output("USR3", GPIO.LOW)



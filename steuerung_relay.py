import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
while True:
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)
    GPIO.cleanup()
GPIO.cleanup()
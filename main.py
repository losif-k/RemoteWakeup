import RPi.GPIO as GPIO
import time
powersw = 14
resetsw = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(powersw, GPIO.OUT)
GPIO.setup(resetsw, GPIO.OUT)
GPIO.output(powersw, GPIO.HIGH)
GPIO.output(resetsw, GPIO.HIGH)
sw = input()
if sw.isdigit() and int(sw) is (14 or 15):
    if int(sw) is 14:
        print("Shorted : 14")
        GPIO.output(powersw, GPIO.LOW)
        time.sleep(1)
        GPIO.output(powersw, GPIO.HIGH)
    if int(sw) is 15:
        print("Shorted : 14")
        GPIO.output(resetsw, GPIO.LOW)
        time.sleep(1)
        GPIO.output(resetsw, GPIO.HIGH)

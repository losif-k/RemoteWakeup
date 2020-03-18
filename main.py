import RPi.GPIO as GPIO
import time
powersw = 14
resetsw = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(powersw, GPIO.OUT)
GPIO.setup(resetsw, GPIO.OUT)
GPIO.output(powersw, GPIO.HIGH)
GPIO.output(resetsw, GPIO.HIGH)
sw = input()
while True:
    if sw.isdigit() and int(sw) is (14 or 15):
        if int(sw) is 14:
            print("Shorted : 14")
            GPIO.output(powersw, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(powersw, GPIO.HIGH)
        if int(sw) is 15:
            print("Shorted : 15")
            GPIO.output(resetsw, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(resetsw, GPIO.HIGH)

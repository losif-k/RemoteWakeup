import RPi.GPIO as GPIO
import time
from datetime import datetime
import asyncio

powersw = 14
resetsw = 15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(powersw, GPIO.OUT)
GPIO.setup(resetsw, GPIO.OUT)
GPIO.output(powersw, GPIO.HIGH)
GPIO.output(resetsw, GPIO.HIGH)


def autowakeup():
    global powersw, resetsw
    while True:
        try:
            date_time = datetime.now()
            date_time.strftime("%H%M")
            if date_time == "0900":
                GPIO.output(powersw, GPIO.LOW)
                time.sleep(0.5)
                GPIO.output(powersw, GPIO.HIGH)
            print(f"{'0900'} and {date_time} / {date_time == '0900'}")
        except KeyboardInterrupt:
            GPIO.output(powersw, GPIO.HIGH)
            GPIO.output(resetsw, GPIO.HIGH)
            GPIO.cleanup()
            return


'''
async def main():
    while True:
        try:
            sw = input()
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

        else:
            continue
'''

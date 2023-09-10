import RPi.GPIO as GPIO
import time

PIN_RELAY = 2 

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_RELAY, GPIO.OUT)

def light_on():
    GPIO.output(PIN_RELAY, GPIO.HIGH)
    print("Lámpara encendida")

def light_off():
    GPIO.output(PIN_RELAY, GPIO.LOW)
    print("Lámpara apagada")

light_off()
time.sleep(2)
light_on()
time.sleep(2)
light_off()
time.sleep(2)

GPIO.cleanup()
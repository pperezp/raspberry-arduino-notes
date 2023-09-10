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

def show_menu():
    print("----------------")
    print("1.- Encender")
    print("2.- Apagar")
    print("3.- Salir")

while True:
    show_menu()
    option = int(input("OP:"))
    
    if option == 1:
        light_on()
    elif option == 2:
        light_off()
    elif option == 3:
        break


GPIO.cleanup()

import RPi.GPIO as GPIO

BUTTON_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)

try:
    while True:
        GPIO.wait_for_edge(BUTTON_PIN, GPIO.FALLING)
        print("¡Botón pulsado!")

except:
    GPIO.cleanup()

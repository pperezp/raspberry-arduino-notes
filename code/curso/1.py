import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

end = False

while not end:
    char = input("Letra: ")
    
    if char == "a":
        GPIO.output(2, GPIO.HIGH)
    elif char == "b":
        GPIO.output(2, GPIO.LOW)
    elif char == "z":
        end = True
        
print("Fin de programa")
GPIO.cleanup()
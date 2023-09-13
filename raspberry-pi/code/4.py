from gpiozero import Button
from signal import pause

BUTTON_PIN = 2
button = Button(BUTTON_PIN)
count = 0

def button_pressed():
    global count
    count += 1
    print("Botón presionado! " + str(count))
    
button.when_pressed = button_pressed

pause()
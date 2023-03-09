# Einfügung von Bibliotheken & setup für die GPIO Pins
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

# An / Aus - Funktion für die GPIO Pins
def LED(outputnumber):
    GPIO.output(outputnumber, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(outputnumber, GPIO.LOW)
    GPIO.cleanup()

# UI
print(16*"#","Menü",16*"#")
print()
print(" vorwärts:          fwd")
print(" rüchkwärts:        bwd")
print(" linksdrehen:      left")
print(" rechtsdrehen:    right")
print()
print(38*"#")
print()

# Zustandsbericht LED je nach Fahrtrichtung
Fahrrichtung = input("Wählen Sie eine Fahrtrichtung durch \nEingabe des jeweiligen Küzrzels aus: ")
if Fahrrichtung == "fwd":
    LED(outputnumber=31)
    print("LED1")
elif Fahrrichtung == "bwd":
    LED(outputnumber=11)
    print("LED2")
elif Fahrrichtung == "left":
    LED(outputnumber=13)
    print("LED3")
elif Fahrrichtung == "right":
    LED(outputnumber=15)
    print("LED4")
else:
    print("nicht erkannt")

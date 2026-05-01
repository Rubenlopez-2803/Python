from microbit import *

# Imagen tipo cruz (más visible que un solo LED)
cruz = Image("00900:"
             "00900:"
             "99999:"
             "00900:"
             "00900")

while True:
    if button_a.is_pressed():
        display.show(cruz)   # Mostrar imagen

    if button_b.is_pressed():
        display.clear()      # Apagar todo

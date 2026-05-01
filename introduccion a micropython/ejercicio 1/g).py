from microbit import *

while True:
    # Encender
    display.set_pixel(1, 1, 9)
    display.set_pixel(1, 3, 9)
    display.set_pixel(3, 1, 9)
    display.set_pixel(3, 3, 9)
    sleep(500)

    # Apagar
    display.set_pixel(1, 1, 0)
    display.set_pixel(1, 3, 0)
    display.set_pixel(3, 1, 0)
    display.set_pixel(3, 3, 0)
    sleep(500)

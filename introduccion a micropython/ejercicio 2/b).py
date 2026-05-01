from microbit import *

while True:
    display.clear()
    for y in range(5):          # filas
        for x in range(5):      # columnas
            display.set_pixel(x, y, 9)
            sleep(100)

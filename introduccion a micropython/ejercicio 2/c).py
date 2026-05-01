from microbit import *

while True:
    display.clear()
    for y in reversed(range(5)):
        for x in reversed(range(5)):
            display.set_pixel(x, y, 9)
            sleep(100)

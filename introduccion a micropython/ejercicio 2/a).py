from microbit import *

peque = Image("00000:"
              "00000:"
              "00900:"
              "00000:"
              "00000")

medio = Image("00000:"
              "09990:"
              "09090:"
              "09990:"
              "00000")

grande = Image("99999:"
               "90009:"
               "90009:"
               "90009:"
               "99999")

anim = [peque, medio, grande, medio]

while True:
    display.show(anim, delay=200, loop=True)

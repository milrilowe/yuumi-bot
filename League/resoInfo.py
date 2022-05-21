import pyautogui as auto
from pynput.mouse import Controller, Listener
import time
from ahk import AHK
from pynput.keyboard import Key, Listener
import socket

ahk = AHK()
mouse = Controller()

#Just used to aid in gathering pixel and coordinate data
time.sleep(2)


try:
    while True:
        x1, y1 = auto.position()
        x2, y2 = mouse.position
        position1Str = 'X: ' + str(x1).rjust(4) + ' Y: ' + str(y1).rjust(4)
        position2Str = 'X: ' + str(x1).rjust(4) + ' Y: ' + str(y1).rjust(4)
        print(position1Str, end='')
        print('\b' * len(position1Str), end='', flush=True)

except KeyboardInterrupt:
    print('\n')
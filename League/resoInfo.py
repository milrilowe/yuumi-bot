import pyautogui as auto
import time
from ahk import AHK
from pynput.keyboard import Key, Listener
import socket

ahk = AHK()

#Just used to aid in gathering pixel and coordinate data
time.sleep(2)

ahk.key_press('@')

print(socket.gethostbyname(socket.gethostname()))
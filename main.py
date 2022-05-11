import convert
from ahk import AHK

ahk = AHK()

red = (255, 0, 0)

coord = (0, 0)

inGame = False

#Currently, will only run if I give red border
if convert.toRGB(coord) == red:
    inGame = True

def inGame():
    return inGame
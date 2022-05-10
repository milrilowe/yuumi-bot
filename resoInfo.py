import pyautogui as auto
import time, keyboard
import yuumi
from ahk import AHK

ahk = AHK()





time.sleep(2)

yuumi = yuumi.Yuumi()

if(yuumi.hasQ()):
    print('hasQ')
else:
    print('noQ')


if(yuumi.hasW()):
    print('hasW')
else:
    print('noW')


if(yuumi.hasE()):
    print('hasE')
else:
    print('noE')


if(yuumi.hasR()):
    print('hasR')
else:
    print('noR')


if(yuumi.hasD()):
    print('hasD')
else:
    print('noD')


if(yuumi.hasF()):
    print('hasF')
else:
    print('noF')

try:
    while True:
        x, y = auto.position()
        rgb = ahk.pixel_get_color(x, 975)
        rgb = rgb[2:]
        r, g, b = tuple(int(rgb[i:i+2], 16) for i in (0, 2, 4))
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + ' R: ' + str(r).rjust(4) + ' G: ' + str(g).rjust(4) + ' B: ' +str(b).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')



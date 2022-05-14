import pyautogui as auto
import time
import yuumi
from ahk import AHK

ahk = AHK()

time.sleep(2)

yuumi = yuumi.Yuumi()
i = 0
try:
    while True:
        x, y = auto.position()
        rgb = ahk.pixel_get_color(x, 975)
        rgb = rgb[2:]
        r, g, b = tuple(int(rgb[i:i+2], 16) for i in (0, 2, 4))
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + ' R: ' + str(r).rjust(4) + ' G: ' + str(g).rjust(4) + ' B: ' +str(b).rjust(4)
        #print(positionStr, end='')
        #print('\b' * len(positionStr), end='', flush=True)

        
        if i == 0:
            for item in yuumi.toBuy:
                print (item.rgb)
                i += 1
        
except KeyboardInterrupt:
    print('\n')
import pyautogui as auto
import time, keyboard
import yuumi

try:
    while True:
        x, y = auto.position()
        r,g,b = auto.pixel(828, 975)

        print(str(r) + ', ' + str(g) + ', ' + str(b))

        yuum = yuumi.Yuumi()

        if(yuum.hasW()):
            yuum.attach()

        if keyboard.is_pressed('q'):
            print('you quit')
            break

except KeyboardInterrupt:
    print('\n')
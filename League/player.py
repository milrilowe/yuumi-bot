import time
import yuumi
import menu

#This shouldn't have any coordinate or pixel values.  It should pretty much be all in English e.g. if yuumi.hasW : yuumi.attach etc.
time.sleep(2)

yuumi = yuumi.Yuumi()

print("Hello")

while True:
    time.sleep(2)

    if yuumi.inShop() :
        yuumi.shop()

    yuumi.attach()

    while(yuumi.isAttached()):
        yuumi.heal()
        yuumi.levelUp()
     
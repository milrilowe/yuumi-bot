import time
import yuumi
import main

#This shouldn't have any coordinate or pixel values.  It should pretty much be all in English e.g. if yuumi.hasW : yuumi.attach etc.
time.sleep(2)

yuumi = yuumi.Yuumi()

while main.inGame:
    if(not yuumi.isAttached()):
        yuumi.initShop()
        yuumi.attach()
        while(not yuumi.isAttached()):
            time.sleep(1)
            print('sleeping')

    if(yuumi.isAttached()):
        yuumi.heal()
        yuumi.levelUp()

print('Q')
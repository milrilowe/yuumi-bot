import time
import yuumi

#This shouldn't have any coordinate or pixel values.  It should pretty much be all in English e.g. if yuumi.hasW : yuumi.attach etc.

yuumi = yuumi.Yuumi()

#Init shop
    #Dark Seal
    #2x Control Wards
    #Sweeper
yuumi.initShop()


while True:
    if(not yuumi.isAttached()):
        #shop()
        yuumi.attach(3)

    if(yuumi.isAttached()):
        yuumi.heal()
    
    if(yuumi.hasQ()):
        print('Q')
        break
        #attached logic 


#Some kind of loop
    #Attach
    #Heal
        #Check HP
    #Level abilities
    #Shop
    

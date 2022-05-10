from ahk import AHK

import convert
import champion

ahk = AHK()

class Yuumi:

    def __init__(self):
        self.champion = champion.Champion(3) #Who Yuumi attaches herself to - initialized as '3' bc the adc is generally the 3rd portrait

        #These are all the necessary x,y coordinates as well as RGB values of abilities and summoner spells
        self.ABILITY_Y_COORD = 975
        self.SUMMONER_Y_COORD = 975
        self.Q_X_COORD = 762
        self.W_X_COORD = 828
        self.E_X_COORD = 893
        self.R_X_COORD = 959
        self.D_X_COORD = 1025
        self.F_X_COORD = 1075
        self.Q_RGB = (251, 223, 69)         #Color changes when unattached - this is attached
        self.W_RGB = (49, 26, 135)          #Color of W while yuumi is unattached to someone
        self.W_ATTACHED_RGB = (21, 98, 181) #Color of W while yuumi is attached to someone
        self.E_RGB = (8, 115, 96)
        self.R_RGB = (118, 52, 173)
        self.D_RGB = (28, 16, 4)
        self.F_RGB = (239, 212, 119)

        #These are all the necessary x,y coordinates as well as RGB values of items -- OR DOES IT EVEN BELONG HERE?!
        self.INIT_Y = 543
        self.INIT_DARKSEAL_X = 933
        self.INIT_CONTROLWARD_X = 985
    
    #Init Shop
    def initShop(self):
        self.openShop()
        self.buyDarkSeal()
        self.buyControlWard()
        self.buyControlWard()
        self.closeShop()

    #Status
    def hasQ(self):
        if(convert.toRGB(self.Q_X_COORD, self.ABILITY_Y_COORD) == self.Q_RGB) :
            return True 
        return False

    def hasW(self):
        if(convert.toRGB(self.W_X_COORD, self.ABILITY_Y_COORD) == self.W_RGB) :
            return True
        return False

    def hasE(self):
        if(convert.toRGB(self.E_X_COORD, self.ABILITY_Y_COORD) == self.E_RGB) :
            return True
        return False

    def hasR(self):
        if(convert.toRGB(self.R_X_COORD, self.ABILITY_Y_COORD) == self.R_RGB) :
            return True
        return False

    def hasD(self):
        if(convert.toRGB(self.D_X_COORD, self.ABILITY_Y_COORD) == self.D_RGB) :
            return True
        return False
    
    def hasF(self):
        if(convert.toRGB(self.F_X_COORD, self.ABILITY_Y_COORD) == self.F_RGB) :
            return True
        return False


    def buyDarkSeal(self):
        if(self.isShopOpen):
            ahk.right_click(self.INIT_DARKSEAL_X, self.INIT_Y)
    
    def buyControlWard(self):
        if(self.isShopOpen):
            ahk.right_click(self.INIT_CONTROLWARD_X, self.INIT_Y)

    #Attach/Detach
    def isAttached(self):
        if convert.toRGB(self.W_X_COORD, self.ABILITY_Y_COORD) == self.W_ATTACHED_RGB:
            return True
        return False

    def attach(self):
        if self.hasW(): 
                ahk.mouse_move(self.champion.getX(), self.champion.getY())
                ahk.key_press(key = 'w')

    #Heal
    def heal(self):
        if self.hasE():
            if self.champ.isMissingHealth():
                ahk.key_press(key = 'e')

    

    #Helper functions
    def openShop(self):
        ahk.key_press(key = 'p')

    def closeShop(self):
        ahk.key_press(key = 'p')

    def isShopOpen(self):
        #add check
        return True
import re
from ahk import AHK

import convert
import champion
import time
import items

ahk = AHK()

class Yuumi:

    def __init__(self):
        self.champion = champion.Champion(1) #Who Yuumi attaches herself to - initialized as '3' bc the adc is generally the 3rd portrait


        #self.toBuy = [items.controlWard, items.darkSeal, items.mikael, items.mejai, items.staff, items.chemtech, items.ardent]


        #These are all the necessary x,y coordinates as well as RGB values of abilities and summoner spells
        self.ABILITY_Y_COORD = 975
        self.LEVELUP_Y_COORD = 922
        self.SUMMONER_Y_COORD = 975
        self.HEALTH_Y_COORD = 1040
        self.MANA_Y_COORD = 1060

        self.HEALTH_MANA_X = 1094

        self.ISINSHOP_Y = 1057
        self.ISINSHOP_X = 1129
        
        self.P_X_COORD = 770
        self.Q_X_COORD = 762
        self.W_X_COORD = 828
        self.E_X_COORD = 893
        self.R_X_COORD = 958
        self.D_X_COORD = 1025
        self.F_X_COORD = 1075

        self.P = (self.P_X_COORD, self.ABILITY_Y_COORD)
        self.Q = (self.Q_X_COORD, self.ABILITY_Y_COORD)
        self.W = (self.W_X_COORD, self.ABILITY_Y_COORD)
        self.E = (self.E_X_COORD, self.ABILITY_Y_COORD)
        self.R = (self.R_X_COORD, self.ABILITY_Y_COORD)

        self.D = (self.D_X_COORD, self.SUMMONER_Y_COORD)
        self.F = (self.F_X_COORD, self.SUMMONER_Y_COORD)

        self.LEVEL_Q = (self.Q_X_COORD, self.LEVELUP_Y_COORD)
        self.LEVEL_W = (self.W_X_COORD, self.LEVELUP_Y_COORD)
        self.LEVEL_E = (self.E_X_COORD, self.LEVELUP_Y_COORD)
        self.LEVEL_R = (self.R_X_COORD, self.LEVELUP_Y_COORD)

        self.FULLHEALTH = (self.HEALTH_MANA_X, self.HEALTH_Y_COORD)
        self.FULLMANA = (self.HEALTH_MANA_X, self.MANA_Y_COORD)

        self.ISINSHOP = (self.ISINSHOP_X, self.ISINSHOP_Y)

        
        self.P_RGB = (54, 100, 228)
        self.Q_RGB = (251, 223, 69)         #Color changes when unattached - this is attached
        self.W_RGB = (49, 26, 135)          #Color of W while yuumi is unattached to someone
        self.W_ATTACHED_RGB = (21, 98, 181) #Color of W while yuumi is attached to someone
        self.E_RGB = (8, 115, 96)
        self.R_RGB = (127, 58, 177)
        self.D_RGB = (28, 16, 4)            #Exhaust - will need an init to determine in future in case we want a different summoner
        self.F_RGB = (239, 212, 119)        #Ignite - will need an init to determine in future in case we want a different summoner

        self.LEVELUP_RGB = (33, 36, 33) #If can level, this pixel is this color

        self.FULL_RGB = (192, 525, 250)

        self.ISINSHOP_RGB = (183, 159, 87)

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

    #Status of abilities
    def hasP(self):
        if(convert.toRGB(self.P) == self.P_RGB) :
            return True 
        return False
        
    def hasQ(self):
        if(convert.toRGB(self.Q) == self.Q_RGB) :
            return True 
        return False

    def hasW(self):
        if(convert.toRGB(self.W) == self.W_RGB) :
            return True
        return False

    def hasE(self):
        if(convert.toRGB(self.E) == self.E_RGB) :
            return True
        return False

    def hasR(self):
        if(convert.toRGB(self.R) == self.R_RGB) :
            return True
        return False

    def hasD(self):
        if(convert.toRGB(self.D) == self.D_RGB) :
            return True
        return False
    
    def hasF(self):
        if(convert.toRGB(self.F) == self.F_RGB) :
            return True
        return False
    
    def manaIsFull(self):
        if convert.toRGB(self.FULLMANA) == self.FULL_RGB:
            return True
        return False

    def healthIsFull(self):
        if convert.toRGB(self.FULLHEALTH) == self.FULL_RGB:
            return True
        return False

    #Shop
    def inShop(self):
        if convert.toRGB(self.ISINSHOP) == self.ISINSHOP_RGB:
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
        if convert.toRGB(self.W) == self.W_ATTACHED_RGB:
            return True
        return False

    def attach(self):
        if self.hasW(): 
                ahk.mouse_move(self.champion.getX(), self.champion.getY())
                ahk.key_press(key = 'w')
        while not self.isAttached():
            time.sleep(1)

    #Heal
    def heal(self):
        if self.hasE():
            if self.champion.isMissingHealth():
                ahk.key_press(key = 'e')

    #Level Up
    def levelUp(self):
        ahk.click(self.canLevel())
            

    def canLevel(self):
        if convert.toRGB(self.LEVEL_R) == self.LEVELUP_RGB:
            return self.LEVEL_R
        elif convert.toRGB(self.LEVEL_E) == self.LEVELUP_RGB:
            return self.LEVEL_E
        elif convert.toRGB(self.LEVEL_W) == self.LEVELUP_RGB:
            return self.LEVEL_W
        elif convert.toRGB(self.LEVEL_Q) == self.LEVELUP_RGB:
            return self.LEVEL_Q

        pass
    

    #Helper functions
    def openShop(self):
        ahk.key_press(key = 'p')

    def closeShop(self):
        ahk.key_press(key = 'p')

    def isShopOpen(self):
        #add check
        return True
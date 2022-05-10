from contextlib import nullcontext
from operator import truediv
from types import WrapperDescriptorType
from ahk import AHK

ahk = AHK()

class Yuumi:

    def __init__(self):
        self.itemOne = self.itemTwo = self.itemThree = self.itemFour = self.itemFive = self.itemSix = self.ward = self.lastAttach = None

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

        #These are all the necessary x,y coordinates of teammates' icons
        self.CHAMPION_ICON_Y = 600
        self.CHAMPION_ONE_X = 1570
        self.CHAMPION_TWO_X = 1680
        self.CHAMPION_THREE_X = 1790
        self.CHAMPION_FOUR_X = 1900

        pass

    #Setters -- These will have to be incredibly complex actually - will involve buying from shop!.......

    def setItemOne(self, itemOne):
        self.itemOne = itemOne

    def setItemTwo(self, itemTwo):
        self.itemTwo = itemTwo

    def setItemThree(self, itemThree):
        self.itemThree = itemThree

    def setItemFour(self, itemFour):
        self.itemFour = itemFour

    def setItemFive(self, itemFive):
        self.itemFive = itemFive

    def setItemSix(self, itemSix):
        self.itemSix = itemSix

    def setWard(self, ward):
        self.ward = ward

    #Getters -- Need to eventually add like, a dictionary so convert RGB into actual item objects

    def getItemOne(self):
        return self.itemOne

    def getItemTwo(self):
        return self.itemTwo
    
    def getItemThree(self):
        return self.itemThree
    
    def getItemFour(self):
        return self.itemFour
    
    def getItemFive(self):
        return self.itemFive
    
    def getItemSix(self):
        return self.itemSix
    
    def getWard(self):
        return self.ward

    #Status
    def hasQ(self):
        if(self.getRGB(self.Q_X_COORD, self.ABILITY_Y_COORD) == self.Q_RGB) :
            return True 
        return False

    def hasW(self):
        if(self.getRGB(self.W_X_COORD, self.ABILITY_Y_COORD) == self.W_RGB) :
            return True
        return False

    def hasE(self):
        if(self.getRGB(self.E_X_COORD, self.ABILITY_Y_COORD) == self.E_RGB) :
            return True
        return False

    def hasR(self):
        if(self.getRGB(self.R_X_COORD, self.ABILITY_Y_COORD) == self.R_RGB) :
            return True
        return False

    def hasD(self):
        if(self.getRGB(self.D_X_COORD, self.ABILITY_Y_COORD) == self.D_RGB) :
            return True
        return False
    
    def hasF(self):
        if(self.getRGB(self.F_X_COORD, self.ABILITY_Y_COORD) == self.F_RGB) :
            return True
        return False
    

    #Shop
    def initShop(self):
        self.openShop()
        self.buyDarkSeal()
        self.buyControlWard()
        self.buyControlWard()
        self.closeShop()

    def openShop(self):
        ahk.key_press(key = 'p')

    def closeShop(self):
        ahk.key_press(key = 'p')

    def isShopOpen(self):
        #add check
        return True

    def buyDarkSeal(self):
        if(self.isShopOpen):
            ahk.right_click(self.INIT_DARKSEAL_X, self.INIT_Y)
    
    def buyControlWard(self):
        if(self.isShopOpen):
            ahk.right_click(self.INIT_CONTROLWARD_X, self.INIT_Y)



    #Heal
        def heal(self):
            pass
    #Attach/Detach
    def isAttached(self):
        if self.getRGB(self.W_X_COORD, self.ABILITY_Y_COORD) == self.W_ATTACHED_RGB:
            return True
        return False

    def attach(self, champ): #Will need a second parameter to determine which teammate
        if self.hasW(): 
            if champ == 1:
                ahk.mouse_move(self.CHAMPION_ONE_X, self.CHAMPION_ICON_Y)
                self.lastAttach = 1
            if champ == 2:
                ahk.mouse_move(self.CHAMPION_TWO_X, self.CHAMPION_ICON_Y)
                self.lastAttach = 2
            if champ == 3:
                ahk.mouse_move(self.CHAMPION_THREE_X, self.CHAMPION_ICON_Y)
                self.lastAttach = 3
            if champ == 4:
                ahk.mouse_move(self.CHAMPION_FOUR_X, self.CHAMPION_ICON_Y)
                self.lastAttach = 4

            ahk.key_press(key = 'w')

    def heal(self):
        if self.hasE():
            if self.lastAttach == 1: 
                ahk.key_press(key = 'e')
            if self.lastAttach == 2: 
                ahk.key_press(key = 'e')
            if self.lastAttach == 3: 
                ahk.key_press(key = 'e')
            if self.lastAttach == 4: 
                ahk.key_press(key = 'e')


    #AHK returns hexadecimal values whereas I'd recorded all the constants as RGB values, so conversion necessary
    def getRGB(self, x, y):
        ahk.pixel_get_color(x, y)
        h = ahk.pixel_get_color(x, y)
        h = h[2:]
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
from contextlib import nullcontext
from types import WrapperDescriptorType


class Yuumi:

    def __init__(itemOne, itemTwo, itemThree, itemFour, itemFive, itemSix, ward):
    
        itemOne, itemTwo, itemThree, itemFour, itemFive, itemSix, ward = None, None, None, None, None, None, None

        #Setters -- These will have to be incredibly complex actually.......
        
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

        #Getters

        def getItemOne(self):
            return itemOne

        def getItemTwo(self):
            return itemTwo
        
        def getItemThree(self):
            return itemThree
        
        def getItemFour(self):
            return itemFour
        
        def getItemFive(self):
            return itemFive
        
        def getItemSix(self):
            return itemSix
        
        def getWard(self):
            return ward

        #Status

        def hasQ():
            return False

        def hasW():
            return False

        def hasE():
            return False

        def hasR():
            return False

        
        
        
        


import convert

class Champion :

    CHAMPION_ICON_Y = 600
    CHAMPION_ONE_X = 1570
    CHAMPION_TWO_X = 1680
    CHAMPION_THREE_X = 1790
    CHAMPION_FOUR_X = 1900

    healthX = 0
    healthY = 0
    missingHealth = (0, 0, 0)


    def __init__(self, pos):     
        y = self.CHAMPION_ICON_Y

        self.set(pos)
    
    def getY(self):
        return self.y
    
    def getX(self):
        return self.get
    
    def getPos(self):
        return self.pos
    
    def set(self, pos):
        self.pos = pos

        if pos == 1:
            x = self.CHAMPION_ONE_X
        if pos == 2:
            x = self.CHAMPION_TWO_X
        if pos == 3:
            x = self.CHAMPION_THREE_X
        if pos == 4:
            x = self.CHAMPION_FOUR_X
    
    def isMissingHealth(self):
        if convert.toRGB(self.healthX, self.healthY) == self.missingHealth:
            return True
        return False
    

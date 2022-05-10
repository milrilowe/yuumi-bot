import convert

class Champion :

    CHAMPION_ICON_Y = 600
    HEALTH_Y = 631
    CHAMPION_ONE_X = 1570
    CHAMPION_TWO_X = 1680
    CHAMPION_THREE_X = 1790
    CHAMPION_FOUR_X = 1900
    HEALTH_ONE_X = 1613
    HEALTH_TWO_X = 1710
    HEALTH_THREE_X = 1807
    HEALTH_FOUR_X = 1904

    missingHealth = (16, 16, 16)


    def __init__(self, pos):     
        self.y = self.CHAMPION_ICON_Y

        self.set(pos)
    
    def getY(self):
        return self.y
    
    def getX(self):
        return self.x
    
    def getPos(self):
        return self.pos
    
    def set(self, pos):
        self.pos = pos

        if pos == 1:
            self.x = self.CHAMPION_ONE_X
        elif pos == 2:
            self.x = self.CHAMPION_TWO_X
        elif pos == 3:
            self.x = self.CHAMPION_THREE_X
        elif pos == 4:
            self.x = self.CHAMPION_FOUR_X
        else:
            self.x = None
    
    def isMissingHealth(self):
        if convert.toRGB(self.healthX, self.healthY) == self.missingHealth:
            return True
        return False
    

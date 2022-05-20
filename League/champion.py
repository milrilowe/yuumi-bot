import convert

class Champion :

    CHAMPION_ICON_Y = 600
    HEALTH_Y = 631

    #Icon x values
    CHAMPION_ONE_X = 1570
    CHAMPION_TWO_X = 1680
    CHAMPION_THREE_X = 1790
    CHAMPION_FOUR_X = 1900

    #Health bar x values (last pixel of green)
    HEALTH_ONE_X = 1613
    HEALTH_TWO_X = 1710
    HEALTH_THREE_X = 1807
    HEALTH_FOUR_X = 1904

    missingHealth_RGB = (16, 16, 16)



    def __init__(self, pos):     
        self.set(pos)
    
    def getY(self):
        return self.icon[1]
    
    def getX(self):
        return self.icon[0]
    
    def getPos(self):
        return self.pos
    
    def set(self, pos):
        self.pos = pos

        if pos == 1:
            self.icon = (self.CHAMPION_ONE_X, self.CHAMPION_ICON_Y)
            self.missingHealth = (self.HEALTH_ONE_X, self.HEALTH_Y)
        elif pos == 2:
            self.icon = (self.CHAMPION_ONE_X, self.CHAMPION_ICON_Y)
            self.missingHealth = (self.HEALTH_TWO_X, self.HEALTH_Y)
        elif pos == 3:
            self.icon = (self.CHAMPION_ONE_X, self.CHAMPION_ICON_Y)
            self.missingHealth = (self.HEALTH_THREE_X, self.HEALTH_Y)
        elif pos == 4:
            self.icon = (self.CHAMPION_ONE_X, self.CHAMPION_ICON_Y)
            self.missingHealth = (self.HEALTH_FOUR_X, self.HEALTH_Y)
        else:
            self.x = None
            self.healthX = None
    
    def isMissingHealth(self):
        if convert.toRGB(self.missingHealth) == self.missingHealth_RGB:
            return True
        return False
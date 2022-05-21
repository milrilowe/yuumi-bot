from ahk import AHK

import convert
import champion
import time
from itemSet import ItemSet
from itemComponents import ItemComponents as Component
import socket
import threading

HEADER  = 2
PORT = 5050
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


ahk = AHK()

class Yuumi:

    #These are all the necessary x,y coordinates as well as RGB values of abilities and summoner spells
    ABILITY_Y_COORD = 975
    LEVELUP_Y_COORD = 922
    SUMMONER_Y_COORD = 975
    HEALTH_Y_COORD = 1040
    MANA_Y_COORD = 1060

    HEALTH_MANA_X = 1094

    ISINSHOP_Y = 1057
    ISINSHOP_X = 1129
    
    P_X_COORD = 770
    Q_X_COORD = 762
    W_X_COORD = 828
    E_X_COORD = 893
    R_X_COORD = 958
    D_X_COORD = 1025
    F_X_COORD = 1075

    P = (P_X_COORD, ABILITY_Y_COORD)
    Q = (Q_X_COORD, ABILITY_Y_COORD)
    W = (W_X_COORD, ABILITY_Y_COORD)
    E = (E_X_COORD, ABILITY_Y_COORD)
    R = (R_X_COORD, ABILITY_Y_COORD)

    D = (D_X_COORD, SUMMONER_Y_COORD)
    F = (F_X_COORD, SUMMONER_Y_COORD)

    LEVEL_Q = (Q_X_COORD, LEVELUP_Y_COORD)
    LEVEL_W = (W_X_COORD, LEVELUP_Y_COORD)
    LEVEL_E = (E_X_COORD, LEVELUP_Y_COORD)
    LEVEL_R = (R_X_COORD, LEVELUP_Y_COORD)

    FULLHEALTH = (HEALTH_MANA_X, HEALTH_Y_COORD)
    FULLMANA = (HEALTH_MANA_X, MANA_Y_COORD)

    ISINSHOP = (ISINSHOP_X, ISINSHOP_Y)

    
    P_RGB = (54, 100, 228)
    Q_RGB = (251, 223, 69)         #Color changes when unattached - this is attached
    W_RGB = (49, 26, 135)          #Color of W while yuumi is unattached to someone
    W_ATTACHED_RGB = (21, 98, 181) #Color of W while yuumi is attached to someone
    E_RGB = (8, 115, 96)
    R_RGB = (127, 58, 177)
    D_RGB = (28, 16, 4)            #Exhaust - will need an init to determine in future in case we want a different summoner
    F_RGB = (239, 212, 119)        #Ignite - will need an init to determine in future in case we want a different summoner

    LEVELUP_RGB = (33, 36, 33) #If can level, this pixel is this color

    FULL_RGB = (192, 525, 250)

    ISINSHOP_RGB = (183, 159, 87)

    toBuy = []

    def __init__(self):
        self.champion = champion.Champion(3) #Who Yuumi attaches herself to - initialized as '3' bc the adc is generally the 3rd portrait

        def setToBuy(list):
            itemSet = list

            for i in itemSet:
                if not type(i) == Component:
                        setToBuy(i)          
                else:
                    self.toBuy.append(i)

        setToBuy(ItemSet.itemSet)

        print("[STARTING] server is starting...")
        thread = threading.Thread(target=start)
        thread.start()

    #Status of abilities
    def hasP(self):
        if(convert.toRGB(self.P) == self.P_RGB) :
            return True 
        return False

    def hasQ(self):
        if(convert.toRGB(self.Q) == self.Q_RGB):
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
    def shop(self):
        self.openShop()
        for component in list(self.toBuy):
            time.sleep(0.1)
            if self.canPurchase(component):
                self.purchase(component)
            else:
                self.closeShop()
                break


    #Attach/Detach
    def isAttached(self):
        if convert.toRGB(self.W) == self.W_ATTACHED_RGB:
            return True
        return False

    def attach(self):
        if self.hasW(): 
            ahk.mouse_move(self.champion.getX(), self.champion.getY())
            ahk.key_press(key = 'w')
            

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

    def purchase(self, component):
        ahk.right_click(component.coord)
        ahk.mouse_move(0,0) #Prevents mouse from triggering drop-down that covers items
        self.toBuy.remove(component)

    def canPurchase(self, component):
        return convert.toRGB(component.coord) == component.rgb

    def inShop(self):
        if convert.toRGB(self.ISINSHOP) == self.ISINSHOP_RGB:
            return True
        return False


def hypnosis(msg):
    input = msg[0]
    coord = msg[1:].split(',')

    print(f'Press {input} @ ({coord})')
    ahk.mouse_move(coord)
    #Because of this line, code doesn't work unless you use a separate computer
    ahk.key_press(key = input)
        


def handle_client(conn, addr):
    print(f"[NEW CONNECTION {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            hypnosis(msg)

    conn.close()


def start():
    server.listen(1)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()

        conn.send(bytes("accepted"))

        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
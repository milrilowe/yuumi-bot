import itemComponent as item
import enum

class Items (enum.Enum):
    
    DARK_SEAL = [item.darkSeal]
    CONTROL_WARD = [item.controlWard]
    FAERIE_CHARM = [item.faerieCharm]
    NULL_MAGIC_MANTLE = [item.nullMagicMantle]
    AMP_TOME = [item.ampTome]

    OBLIVION_ORB = [AMP_TOME, item.oblivionOrb]
    BANDLEGLASS_MIRROR = [FAERIE_CHARM, AMP_TOME, item.bandleglassMirror]
    FORBIDDEN_IDOL = [FAERIE_CHARM, item.forbiddenIdol]
    NEGATRON_CLOAK = [AMP_TOME, item.negatronCloak]


    
    MIKAELSBLESSING = [FORBIDDEN_IDOL, NEGATRON_CLOAK, item.mikaelsBlessing]
    MEJAIS = [DARK_SEAL, item.mejais]
    STAFF_OF_FLOWING_WATER = [FORBIDDEN_IDOL, AMP_TOME, AMP_TOME, item.staffOfFlowingWater]
    CHEMTECH_PUTRIFIER = [OBLIVION_ORB, item.chemtechPutrifier]
    ARDENT_CENSER = [FORBIDDEN_IDOL, AMP_TOME, AMP_TOME, item.ardentCenser]



    def __init__(self, item):
        self.components = []
        self.item = item
    
    def idk(self):
        if self.item == self.darkSeal:
            pass
        elif self.item == self.Mikael:
            #Instead of each compenent, should be another Item object
            self.component.push(self.faerieCharm) 
            self.component.push(self.forbiddenIdol)
            self.component.push(self.NullMagicMantle)
            #self.component.push(self.Negatron Cloak)

    

    



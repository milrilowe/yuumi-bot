from itemComponents import ItemComponents as Component
from enum import Enum

class Items (Enum):

    DARK_SEAL = [Component.darkSeal]
    CONTROL_WARD = [Component.controlWard]
    FAERIE_CHARM = [Component.faerieCharm]
    NULL_MAGIC_MANTLE = [Component.nullMagicMantle]
    AMP_TOME = [Component.ampTome]

    OBLIVION_ORB = [AMP_TOME, Component.oblivionOrb]
    BANDLEGLASS_MIRROR = [FAERIE_CHARM, AMP_TOME, Component.bandleglassMirror]
    FORBIDDEN_IDOL = [FAERIE_CHARM, Component.forbiddenIdol]
    NEGATRON_CLOAK = [NULL_MAGIC_MANTLE, Component.negatronCloak]
    
    MIKAELS_BLESSING = [FORBIDDEN_IDOL, NEGATRON_CLOAK, Component.mikaelsBlessing]
    MEJAIS = [Component.mejais] #We buy a dark seal earlier, so I'm not including it here
    STAFF_OF_FLOWING_WATER = [FORBIDDEN_IDOL, AMP_TOME, AMP_TOME, Component.staffOfFlowingWater]
    CHEMTECH_PUTRIFIER = [BANDLEGLASS_MIRROR, OBLIVION_ORB, Component.chemtechPutrifier]
    ARDENT_CENSER = [FORBIDDEN_IDOL, Component.ardentCenser]

    def __iter__(self):
        itr = self.value.__iter__()
        return itr
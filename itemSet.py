from enum import Enum
from items import Items as Item


class ItemSet(Enum):
    itemSet = [Item.DARK_SEAL, Item.CONTROL_WARD, Item.MIKAELS_BLESSING, Item.MEJAIS, Item.STAFF_OF_FLOWING_WATER, Item.CHEMTECH_PUTRIFIER, Item.ARDENT_CENSER]

    def __iter__(self):
        itr = self.value.__iter__()
        return itr



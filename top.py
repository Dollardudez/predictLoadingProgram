
from item import Item
#top object
class Top(Item):
    def __init__(self, l, w, val, pal, we):
        super().__init__(l, w, we)
        #is it on a pallet?
        self.pallet = pal
        self.value = val

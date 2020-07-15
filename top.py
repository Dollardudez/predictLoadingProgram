
from item import Item
#top object
class Top(Item):
    def __init__(self, l, w, val, pal, we, f):
        super().(self, l, w, we)
        #is it on a pallet?
        self.pallet = pal
        #in a fat box or not?
        self.fat = f
        self.value = val

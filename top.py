
from item import IItem
#top object
class Top(IItem):
    def __init__(self,b_t_p, l, w, val, pal, we):
        super().__init__(b_t_p, l, w, we, val)
        #is it on a pallet?
        self.pallet = pal
        self.value = val
        self.b_t_p = b_t_p

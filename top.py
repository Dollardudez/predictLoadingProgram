
from item import IItem
#top object
class Top(IItem):
    """
    Represents a top. It inherits attributes from the IItem interface.

    Attributes:
        pallet: a boolean value whether or not the top is on a pallet.
        value: the height of the top (in relation to 1 panel)
        length: the length of the item.
        width: the width of the item.
        weight: the weight of the item.
        x: the x position of the item (default = 5).
        y: the y position of the item (default = 5).
        paired: a boolean that is True if the item is paired with another one, False otherwise.
        b_t_p: a string that shows if the item isa base, top, or panel.
    """
    def __init__(self,b_t_p, l, w, val, pal, we):
        """
        Constructor for the Top class
        """
        super().__init__(b_t_p, l, w, we, val)
        #is it on a pallet?
        self.pallet = pal
        self.value = val
        self.b_t_p = b_t_p

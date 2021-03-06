
class IItem:
    """
    the Item class is an interface class for panels, bases, and tops.
    It provides length, width, and height to all of those objects and classifies them all as "Items"

    Attributes:
        length: the length of the item.
        width: the width of the item.
        weight: the weight of the item.
        x: the x position of the item (default = 5).
        y: the y position of the item (default = 5).
        paired: a boolean that is True if the item is paired with another one, False otherwise.
        b_t_p: a string that shows if the item isa base, top, or panel.

    """
    
    def __init__(self,b_t_p, l, w, we, val: int):
        """
        Constructor for the Item interface.
        """
        self.length = l
        self.width = w
        self.weight = we
        self.val = val
        self.x = 5
        self.y = 5
        self.paired = False
        self.b_t_p = b_t_p
        


from item import IItem

#base object
class Base(IItem):
    """
    represents a Base object. It inherits length, width, and weight
    from the Item class

    Attributes:
        length: the length of the item.
        width: the width of the item.
        weight: the weight of the item.
        x: the x position of the item (default = 5).
        y: the y position of the item (default = 5).
        paired: a boolean that is True if the item is paired with another one, False otherwise.
        b_t_p: a string that shows if the item isa base, top, or panel.
        pallet: True or False depending on whether the base is on a pallet.
        type: the type of base (midheight, fullheight, lopro, extreme lopro).
        value: the height (in relation to the height of 1 panel) of the base.
    """
    
    def __init__(self,b_t_p, ty, l, w, we, pal, val):
        """
        Constructor for the Base object.
        """
        super().__init__(b_t_p, l, w, we, val)
        #is it on a pallet?
        self.pallet = pal
        #midheight, fullheight, lopro, extreme lopro.
        self.type = ty
        #height of base in relation to 1 panel.
        self.value = val
        self.b_t_p = b_t_p
        
    def will_2piggy(self, base2):
        if(self.width + base2.width < 100):
            if(self.length < 70 and base2.length < 70 and self.type == base2.type):
                return True
        else: return False


    def will_3piggy(self, base2, base3):
        """
        Method that determines if a base could fit "3 piggy" with 2 other bases.

        Parameters:
            base2: a base object.
            base3: a different base object.

        Returns: a boolean True if the base can 3 piggy with base2 and base3, returns False if otherwise.
        """
        if(self.width + base2.width < 73):
            if(base3.width + self.length  < 100 and base3.width + base2.length  < 100):
                return True
        elif(self.width + base3.width < 73):
            if(base2.width < 40):
                return True
        else: return False
    
    def orient_vertical(self):
        """
        Method that reorients the base to be flipped vertically.
        """
        temp_length = self.length
        self.length = self.width
        self.width = temp_length

    def undo_orient_vertical(self):
        """
        Method that undoes the the orient_vertical method.
        """
        temp_length = self.length
        self.length = self.width
        self.width = temp_length
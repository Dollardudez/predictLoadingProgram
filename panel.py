from item import IItem

#panel object
class Panel(IItem):
    
    """
    Represents a Panel object. It inherits attributes from the IItem interface.

    Attributes:
        value: the heigth of the panel (in relation to one panel). It is ALWAYS 1.
        pallet: a boolean value that is TRue if the panel is on a pallet. False otherwise.
        length: the length of the item.
        width: the width of the item.
        weight: the weight of the item.
        x: the x position of the item (default = 5).
        y: the y position of the item (default = 5).
        paired: a boolean that is True if the item is paired with another one, False otherwise.
        b_t_p: a string that shows if the item isa base, top, or panel.
    """
    
    def __init__(self,b_t_p, l, w, we, pal, val = 1):
        """
        Constructor for the Panel class
		"""
        super().__init__(self,b_t_p, l, w, we, val, x, y, paired)
        self.pallet = pal
        self.value = 1
        self.b_t_p = panel
        
    def will_pair_4wide(self, pan2):
        """
        Method that determines if 2 panels will fit in a 4wide space.

        Parameters:
            pan2: the panel to be checked if it pairs with "self".

        Returns:
            True: if the panels can be paired 4-wide.
            False: if the panels cannot be paired 4-wide.
		"""
        if self.width + pan2.width <= 90 and self.width + pan2.width >= 68 :
            return True
        else : 
            return False
        
        
    def will_pair_3wide(self, pan2):
        """
		"""
        if self.width + pan2.width <= 67 and self.width + pan2.width >= 50 :
            return True
        else :
            return False
        
    def will_pair_2wide(self, pan2):
        """
		"""
        if self.width + pan2.width <= 45 and self.width + pan2.width >= 30 :
            return True
        else :
            return False
            
        

    

#item object
class Item:
    """the Item class is a parent class for panels, bases, and tops.
    It provides length, width, and height to all of those objects"""
    def __init__(self, l, w, we):
        self.length = l
        self.width = w
        self.weight = we
        


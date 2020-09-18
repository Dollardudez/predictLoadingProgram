from item import IItem

class TruckList():
    """
    Represents a particlar slice of the truck.

    Attributes:
        list: a list that holds all of the items that have been placed in that area of the truck.
        height: the current height of that area in the truck (in relation to 1 panel).
        max_height: the maximum height of that area in the truck.
    """

    def __init__(self, max_height):
        """
        Constructor for the TruckList class.
        """
        self.list = []
        self.height = 0
        self.max_height = max_height

    def add_item(self, item):
        """
        Method that adds an item to the TruckList and increases the trucklist height by the value 
        associated with the item's height
        """
        self.list.append(item)
        self.height += int(item.val)

    def peek(self):
        return self.list[0]

    def dequeue(self):
        return self.list.pop(0)





from item import IItem

class TruckList():

    def __init__(self, max_height):
        self.list = []
        self.height = 0
        self.max_height = max_height

    def add_item(self, item):
        self.list.append(item)
        self.height += int(item.val)





import re
from base import Base
from panel import Panel
from top import Top
from linked_list import LinkedList

class Load():
    """ 
    Creates a load object whose Attribute is a list of orders where each
    order holds a list that contains the items in that particular order.

    Attributes:
        entire_load: a list of lists where each list element in "entire_load" is a distinct order of items.
        
    """
    
    def __init__(self):
        """
        The constructor for the Load class.
        """
        self.entire_load = []
        
    def read_base(self, line):
        """
        Method reads in a base creates a Base object from the information provided.

            Parameters:
                line: the line in the text document that contains information to create an instance of a base.

            Returns:
                base: an instance of the Base() class.
        """
        split_line = re.split(', ',line)
        base = Base(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6])
        return base
    
    def read_top(self, line):
        """
        Method reads in a top creates a Top object from the information provided.

            Parameters:
                line: the line in the text document that contains information to create an instance of a top.

            Returns:
                top: an instance of the Top() class.
        """
        split_line = re.split(', ',line)
        top = Top(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5])
        return top
    
    def read_panel(self, line):
        """
        Method reads in a panel creates a Panel object from the information provided.

            Parameters:
                line: the line in the text document that contains information to create an instance of a panel.

            Returns:
                panel: an instance of the Panel() class.
        """
        split_line = re.split(', ',line)
        panel = Panel(split_line[0], split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6])
        return panel
    
    def read_in_load(self, filename, number_of_orders):
        """
        Method that reads in the items that are to be loaded into the truck from a text document, and places those
        items into the Load.list Attribute. Each list within the outer list are separate orders in the truck, each element
        within the inner lists are distinct items within those orders.

        Parameters:
            filename: the path to the file that holds the items to be loaded.
            number_of_orders: the number of orders to be loaded.
        """
        count = 0
        f = open(filename, "r")
        try:
            self.entire_load.append(LinkedList())
            for line in f.readlines()[1:]:
                if("##" in line):
                    count += 1
                    self.entire_load.append(LinkedList())
                    continue
                if("base" in line): self.entire_load[count].insert_node(self.read_base(line))
                if("top" in line): self.entire_load[count].insert_node(self.read_top(line))
                if("panel" in line): self.entire_load[count].insert_node(self.read_panel(line))
        finally:
            f.close()
            
    def count_number_of_orders(self, filename):
        """
        Method that counts the number of orders to be loaded.

        Parameters:
            filename: the path to the file that holds the items to be loaded.

        Returns:
            i: the number of distinct orders to be loaded.
        """
        f = open(filename, "r")
        i = 1;
        try:
            for line in f.readlines():
                if ("##" in line): i = i +1
                    
        finally:
            f.close()
        return i
    
    
        
        
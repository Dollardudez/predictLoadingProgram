import re
from base import Base
from panel import Panel
from top import Top

class Load():
    """ 
    creates a load object that has a public property which is a list of orders where each
    order holds a list that contains the items in the order
    """
    
    def __init__(self):
        self.list = []
        
    def read_base(self, line):
        split_line = re.split(', ',line)
        base = Base(split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6])
        return base
    
    def read_top(self, line):
        split_line = re.split(', ',line)
        top = Top(split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6])
        return top
    
    def read_panel(self, line):
        split_line = re.split(', ',line)
        panel = Panel(split_line[1], split_line[2], split_line[3], split_line[4], split_line[5], split_line[6])
        return panel
    
    def read_in_load(self, filename, number_of_orders):
        count = 0
        f = open(filename, "r")
        try:
            self.list.append([])
            for line in f.readlines()[1:]:
                if("##" in line):
                    count += 1
                    self.list.append([])
                    continue
                if("base" in line): self.list[count].append(self.read_base(line))
                if("top" in line): self.list[number_of_order].append(read_top())
                if("panel" in line): self.list[number_of_order].append(read_panel())
        finally:
            f.close()
            
    def count_number_of_orders(self, filename):
        f = open(filename, "r")
        i = 1;
        try:
            for line in f.readlines():
                if ("##" in line): i = i +1
                    
        finally:
            f.close()
        return i
    
    
        
        
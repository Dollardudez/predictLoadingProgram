# code used from https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList(object):
    """
    A class that represents a linked list
    """
    def __init__(self, head=None):
        self.head = head

    def insert_node(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def copy(self):
        result = LinkedList()
        buffer = self.head
        while buffer.next_node != None:
            result.insert_node(buffer.data)
            buffer = buffer.next_node
        result.insert_node(buffer.data)
        return result


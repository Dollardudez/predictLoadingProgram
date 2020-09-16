# code used from https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/


class Node():
    """
    Represents a node in a linked list.

    Attributes:
            data: the information to be held by the node.
            next_node: a pointer that connects the current node to the node that is next in line.
    """
    def __init__(self, data=None):
        """
        Constructor for the node class.

        Parameters:
            data: the information to be held by the node.
        """
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList():
    """
    A class that represents a linked list.

    Attributes:
            head: the first node in the linked list, default is null.
    """
    def __init__(self, head=None):
        """
        Constructor for the LinkedList class.

        Parameters:
            head: the first node in the linked list, default is null.
        """
        self.head = head

    def insert_node(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def size(self):
        """
        Method that counts the size of a linked list.

        Returns:
            the number of nodes in the linked list as an int.
        """
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
        """
        Method that deletes the node with that specific data from a linked list.
        """
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
        """
        Method that copies one linked list and stores the information in a new linked list.

        Returns:
            the new copy of the linked list
        """
        result = LinkedList()
        buffer = self.head
        while buffer.next_node != None:
            result.insert_node(buffer.data)
            buffer = buffer.next_node
        result.insert_node(buffer.data)
        return result


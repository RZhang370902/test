class Node:
    """An object for string a single node of a linked list.
    Models two attributes - data and the linke to the next node in the list """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
       return "<Node data: %s>" % self.data

class LinkedList:
    """Singly linked list"""
    def __init__(self):
        self.head = None

    def is_empty(self):
      return self.head == None
    
    def size(self):
        """Returns the number of nodes in the list
        Takes O(n) time"""
        current = self.head
        count = 0

        while current:
            count = count + 1
            current = current.next_node

        return count
    def add(self, data):
        """Add new Node containing data at head of the list
            Takes O(1) time"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node



"""l = LinkedList()
N1 = Node(10)
N2 = Node(20)
N1.next_node = N2
l.head = N1          
print(N1, N2, N1.next_node, l.size())
"""

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
print(l.size())
print(l[1])

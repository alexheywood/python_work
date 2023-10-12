#This is an implementation of a linked list

class Node:
    """
    An object that stores information and a reference 
    to the next node within a linked list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data 


class LinkedList:
    """
    A singly liked list which stores Node objects.
    """
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self):
       return self.head == None
    
    def size(self):

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
            
        return count
    
    def add(self, data):
        """
        Adds a new node containing data to the head of the linked list.
        This operation takes constant time N(1).
        @param data, items to be listed
        @return void
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Return the node or 'None' if not found.
        Takes O(n) time.
        """
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        
        return None
    
    def insert(self, data, index):
        """
        Inserts data at the specified index.
        Insertion takes O(1) time but finding the node at the insertion point
        takes O(n) time.
        Takes overall O(n) time.
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)
            current = self.head
            position = index

            while position > 1:
                current = new_node.next_node
                position -= 1

            prev = current
            next = current.next_node
            prev.next_node = new_node
            new_node.next_node = next 


    def remove(self, key):

        current = self.head
        previous_node = None
        found = False

        while current.next_node and not found:

            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node


            elif current.data == key:
                found = True
                previous_node.next_node = current.next_node
            
            else:
                previous_node = current
                current = current.next_node
        
        return current


    def __repr__(self) -> str:
        """
        Return a string representation of the link
        Takes O(n) time.
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '->'.join(nodes)
    


        



    


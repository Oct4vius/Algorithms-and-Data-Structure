class Node:

    """
    An objctect for storign a single node of linked list.
    Models two attributes - data and the link to the next in the list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data


    def __repr__(self):
        return f'<Node data: {self.data}>'
    
class LinkedList:
    """
    Singly linked list
    """

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def size(self):

        """
        Return the number of nodes in the list
        Takes O(n) time
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Takes O(1) time
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):

        """
        Serach for the first node containing data that matches the key
        Return the node or `None` if not found

        Takes O(n) time
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
        Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding node at pooint take O(n) time.
        """

        if(index > self.size()): 
            print('The size of the LinkedList is not that large')
            return 

        if(index == 0):
            self.add(data)
            return
        if(index > 0):
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -=1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):

        """
        Removes Node containing data that matches the key
        Return the node or None if key doesn't exists
        Takes O(n) time
        """

        current = self.head
        previus = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previus.next_node = current.next_node
            else:
                previus = current
                current = current.next_node
        return current
    
    def delete(self, index):

        if(index > self.size() - 1): 
            print('The size of the LinkedList is not that large')
            return 

        current = self.head
        position = index
        previus = None

        if(index == 0):
            self.head = current.next_node
            return current
        
        while position > 0:
            previus = current
            current = current.next_node
            position -=1

        previus.next_node = current.next_node

        return current
        

    def read(self, index):

        if(index > self.size() - 1): 
            print('The size of the LinkedList is not that large')
            return 

        current = self.head
        position = index

        while position > 0:
            current = current.next_node
            position -=1 

        print(current.data)
        
    def __repr__(self):
        """
        Return a string representation of the list.
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
        return  '-> '.join(nodes)

    
class __main__:
    l = LinkedList()
    for i in range(0,10):
        l.add(i + 1)

    l.delete(9)

    l.read(4)

    print(l)
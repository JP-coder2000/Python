class Node:
    def __init__(self,data):
        #We instanciate the data we are given into the node
        self.data = data
        #We create the next and previus pointers
        self.next = None
        self.previus = None

class Doubly_linked_list:

    def __init__(self):
        #This is the first node of the linked list
        self.head = None
        self.tail = None

    #the most common thing is to insert at the end of the list
    def insert_end(self,data):

        new_node = Node(data)
        #if it is the first node, then it is the head and the tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        #if it is not the first node, then we need to update the pointers
        else:
            new_node.previus = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    
    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    
    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previus


list = Doubly_linked_list()

list.insert_end(1)
list.insert_end(2)
list.insert_end(3)
list.insert_end(4)
list.insert_end(5)


list.traverse_forward()
list.traverse_backward()
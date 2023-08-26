class Node:
    # This is how we create a node
    # We need to pass the data to the node
    # 'self' is the node itself
    def __init__(self, data):
        # 'data' is the value of the node
        self.data = data
        # 'next' is the pointer to the next node
        self.next = None
    
class LinkedList:
    def __init__(self):
        # This is the first node of the linked list
        # We can access this node exclusively! We can´t access the other nodes
        self.head = None
        self.num_of_nodes = 0

    def size_of_list(self):
        return self.num_of_nodes
    
    # This is how we insert a node at the start of the linked list
    def insert_start(self, data):
        self.num_of_nodes += 1
        # Create a new node
        new_node = Node(data)

        if self.head is None:
            # If there is no head, then the new node is the head
            self.head = new_node
        else:
            # If there is a head, then the new node is the head and the next node is the previous head
            new_node.next = self.head
            self.head = new_node
    
    def insert_end(self, data):
        self.num_of_nodes += 1
        # Create a new node
        new_node = Node(data)
        
        # If there is no head, then the new node is the head
        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head
            # While there is a next node, we keep going
            while actual_node.next is not None:
                actual_node = actual_node.next
            
            # When there is no next node, we assign the new node to the next node
            actual_node.next = new_node
            
    #this is how we visit every single item in the linked list
    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next
    
    def remove(self,data):
        if self.head is None:
            return #if there is no head, there is nothing to remove
        
        actual_node = self.head
        previous_node = None

        #we need to search for the node to remove
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next
        
        #if we reach the end of the list and we didn´t find the node, we return
        if actual_node is None:
            return
        
        #the node to remove is the head
        if previous_node is None:
            self.head = actual_node.next
        else:
            #this is the code where we remove the node we are looking for
            previous_node.next = actual_node.next

# Create an instance of LinkedList
my_list = LinkedList()

# Insert values into the linked list
my_list.insert_start(20)
my_list.insert_end(34.2)
my_list.insert_start(10)
my_list.insert_end(40)
my_list.insert_start(0)
my_list.insert_end(50)
my_list.insert_start(-10)


# Print the values in the linked list
my_list.traverse()
print("-----------º-----------")

# Remove a value from the linked list
LinkedList.remove(my_list, 20)
my_list.traverse()
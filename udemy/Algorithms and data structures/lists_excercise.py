

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer is not None and fast_pointer.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

    def insert(self, data):

        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node


class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None


list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
list.insert(5)
list.insert(6)
list.insert(7)
list.insert(8)
list.insert(9)

print(list.get_middle_node().data)

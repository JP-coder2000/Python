#Lifo structure
#last in first out

class Stack:
    def __init__(self):
        self.stack = []
    
    # push method which is going to inster element into the stack

    def push(self,data):
        self.stack.append(data)
    
    
    # pop will remove and return the last item we inserted
    def pop(self):

        if self.stack_size() < 1:
            return

        data = self.stack[-1]
        del self.stack[-1]
        return data
    

    #peek return the last item without removing it

    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return self.stack ==[]
    
    def stack_size(self):
        return len(self.stack)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)
print(stack.stack_size())
print(stack.pop())
print(stack.peek())


"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

#LIFO - Last In First Out

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def isEmpty(self):
        return self.storage == []    

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        data = self.storage[-1]
        del self.storage[-1]
        return data


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.__len__())
print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.__len__())
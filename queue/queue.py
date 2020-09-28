"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
#FIFO - first In -> first out

from singly_linked_list import *

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return sum([1 for i in self.storage])

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage.pop(0)


# queue = Queue()
# queue.enqueue(100)
# queue.enqueue(200)
# queue.enqueue(300)
# print(queue.__len__())
# print("Dequeue: ", queue.dequeue())
# print("Dequeue: ", queue.dequeue())
# print(queue.__len__())
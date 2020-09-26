"""
Add a Queue helper class instead of importing a dequeue
Queue() creates a new queue that is empty
It needs no parameters and returns an empty queue

"""

class Queue():
    
    def __init__(self):
        self.queue = []

    # enqueue(item) adds a new item to the rear of the queue. It needs the item and returns nothing
    def enqueue(self, value):
        self.queue.append(value)

    # dequeue() removes the front item from the queue. It needs no parameters and returns the item. The queue is modified
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    
    # size() returns the number of items in the queue. It needs no parameters and returns an integer
    def size(self):
        return len(self.queue)

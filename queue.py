from node import Node

class Queue():
    def __init__(self, value = None, max_size=None):
        self.size = 0
        self.max_size = max_size
        self.head = value
        self.tail = value
    
    def enqueue(self, value):
        node_to_add = Node(value)
        if self.size == self.max_size:
            print("Queue is full")
            return
        if self.size == 0:
            self.tail = node_to_add
            self.head = node_to_add
            self.size += 1
        else:
            self.tail.set_link(node_to_add)
            self.tail = node_to_add
            self.size += 1

    def get_size(self):
        return self.size
    
    def peek(self):
        if self.size <= 0:
            print("Queue empty")
            return
        else:
            print("top value is: " + str(self.head.get_value()))
    
    def dequeue(self):
        if self.size == 0:
            print("Queue empty")
        if self.size == 1:
            value_to_return = self.head.get_value()
            self.head = None
            self.tail = None
            self.size -=1

        else:
            value_to_return = self.head.get_value()
            self.head = self.head.get_link()
            self.size -= 1
            return value_to_return

#test cases
# my_queue = Queue()
# my_queue.enqueue(8)
# my_queue.enqueue(7)
# my_queue.enqueue(6)
# my_queue.enqueue(5)
# my_queue.enqueue(4)
# my_queue.peek()
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.dequeue()
# my_queue.peek()
# my_queue.dequeue()
# my_queue.peek()
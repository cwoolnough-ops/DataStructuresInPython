from node import Node

class Stack():
    def __init__(self,max_size = None):
        self.top = None
        self.size = 0
        self.max_size = max_size

    def peek(self):
        if self.size == 0:
            print("stack is empty")
        else:
            print("top value is: " + str(self.top.get_value()))

    def pop(self):
        if self.size != 0:
            removed_value = self.top
            self.top = self.top.get_link()
            self.size -= 1
            print("you removed: " + str(removed_value.get_value()))
        return removed_value

    def push(self, value):
        if self.size == self.max_size:
            print("stack is full")
            return
        if self.size == 0:
            self.top = Node(value)
            self.size += 1
        else:
            node_to_add = Node(value)
            node_to_add.set_link(self.top)
            self.top = node_to_add
            self.size += 1
#test cases
# tower = Stack()
# tower.push(9)
# tower.push(8)
# tower.push(7)
# tower.push(6)
# tower.peek()
# tower.pop()
# tower.peek()
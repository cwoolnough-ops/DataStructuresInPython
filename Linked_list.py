from node import Node

class LinkedList:
    def __init__(self, value):
        self.head_node = Node(value)
        self.list_length = 0
        if value != None:
            self.list_length += 1

    def get_head_node(self):
        return self.head_node

    def add_new_head(self, value):
        new_head = Node(value, self.head_node)
        self.head_node = new_head
        self.list_length += 1

    def get_length(self):
        return self.list_length
#
    def find_value(self, value):
        current_node = self.head_node
        nodes_found = 0
        while current_node:
            if current_node.get_value() == value:
                nodes_found += 1
                current_node = current_node.get_link()
            else: current_node = current_node.get_link()
        return str(nodes_found) + " nodes with value: " + str(value) + " found."

    def stringify_list(self):
        current_node = self.head_node
        string = ""
        while current_node:
            string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_link()
        return string

    def remove_node(self, removed_value):
        current_node = self.head_node
        previous_node = None
        amount_deleted = 0
        if self.head_node.get_value() == removed_value: #checks if removed_value is head_node
                self.head_node = current_node.get_link()
                self.list_length -= 1
                amount_deleted += 1
                current_node = current_node.get_link()        
        while current_node:
            if current_node.get_value() == removed_value:
                previous_node.link = current_node.get_link()
                self.list_length -= 1
                amount_deleted += 1
            previous_node = current_node
            current_node = current_node.get_link()
        return str(amount_deleted) + " Nodes deleted"
#test cases
# ll = LinkedList(4) 
# ll.add_new_head(8)
# ll.add_new_head(4)
# ll.add_new_head(6)
# ll.add_new_head(5)
# ll.add_new_head(4)
# ll.add_new_head(3)
# ll.add_new_head(2)
# ll.add_new_head(4)
# print(ll.stringify_list())
# print(ll.find_value(4))
# print(ll.remove_node(4))
# print(ll.stringify_list())
# print(ll.find_value(4))

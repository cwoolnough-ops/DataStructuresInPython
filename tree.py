
class TreeNode():
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        print("adding {} as a child to {}".format(child_node.value, self.value))

    def remove_child(self, child_node):
        self.children = [child for child in self.children if child != child_node]
        print("removing {} from {}".format(child_node.value, self.value))

    def traverse(self):
        print("traversing: " + str(self.value))
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop(0)
            nodes_to_visit.extend(current_node.children)
            print(str(current_node.value))

#test cases
# one = TreeNode(1)
# two = TreeNode(2)
# three = TreeNode(3)
# four = TreeNode(4)
# five = TreeNode(5)
# six = TreeNode(6)
# one.add_child(two)
# one.add_child(three)
# two.add_child(four)
# two.add_child(five)
# four.add_child(six)
# one.traverse()
# one.remove_child(two)
# one.traverse()
# two.traverse()
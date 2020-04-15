class MinHeap():
    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    def parent_idx(self, idx):
        return (idx // 2)

    def left_child_index(self, idx):
        return idx * 2 

    def right_child_index(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_index(idx) <= self.count

    def retrieve_min(self):
        if self.count == 0:
            print("empty heap")
            return
        self.count -= 1
        min = self.heap_list[1]
        last_index_value = self.heap_list[-1]
        self.heap_list[1] = last_index_value
        self.heap_list.pop()
        self.heapify_down()
        return min

    def add(self, value):
        self.count += 1
        self.heap_list.append(value)
        self.heapify_up()

    def smaller_child_idx(self, idx):
        if self.right_child_index(idx) > self.count:
            return self.left_child_index(idx)
        else:
            left_child = self.heap_list[self.left_child_index(idx)]
            right_child = self.heap_list[self.right_child_index(idx)]
            if left_child < right_child:
                return self.left_child_index(idx)
            else:
                return self.right_child_index(idx)


    def heapify_up(self):
        if self.count == 1:
            return
        value_checked = self.heap_list[self.count]
        current_index = self.count
        parent_value = self.heap_list[self.parent_idx(current_index)]
        while current_index > 1:
            parent_idx = self.parent_idx(current_index)
            self.heap_list[parent_idx] = value_checked
            self.heap_list[current_index] = parent_value
            current_index = parent_idx
            value_checked = self.heap_list[parent_idx]
            parent_value = self.heap_list[self.parent_idx(current_index)]

    def heapify_down(self):
        current_index = 1
        while self.child_present(current_index):
            parent_value = self.heap_list[current_index]
            smaller_child_value = self.heap_list[self.smaller_child_idx(current_index)]
            if parent_value < smaller_child_value:
                return
            self.heap_list[current_index] = smaller_child_value
            self.heap_list[self.smaller_child_idx(current_index)] = parent_value
            current_index = self.heap_list[self.smaller_child_idx(current_index)]
#test cases
minheap = MinHeap()
minheap.add(4)
minheap.add(10)
minheap.add(15)
minheap.add(20)
print(minheap.heap_list)
minheap.add(8)
print(minheap.heap_list)
print(minheap.retrieve_min())
print(minheap.heap_list)
print(minheap.retrieve_min())
print(minheap.heap_list)
minheap.add(1)
print(minheap.heap_list)

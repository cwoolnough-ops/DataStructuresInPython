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
        while value_checked < parent_value:
            parent_idx = self.parent_idx(current_index)
            self.heap_list[parent_idx] = value_checked
            self.heap_list[current_index] = parent_value
            current_index = parent_idx
            value_checked = self.heap_list[parent_idx]
            parent_value = self.heap_list[self.parent_idx(current_index)]
            if current_index == 1:
                return
            

    def heapify_down(self):
        current_index = 1
        while self.child_present(current_index):
            smaller_child_idx = self.smaller_child_idx(current_index)
            if self.heap_list[current_index] > self.heap_list[smaller_child_idx]:
                temp = self.heap_list[smaller_child_idx]  #smaller childs value
                self.heap_list[smaller_child_idx] = self.heap_list[current_index] #mkes smaller childs value = parent value
                self.heap_list[current_index] = temp  #changes parents value to smaller childs value
                current_index = smaller_child_idx

#test cases
minheap = MinHeap()
minheap.add(4)
minheap.add(10)
minheap.add(15)
minheap.add(20)
minheap.add(21)
minheap.add(22)
minheap.add(23)
minheap.add(24)
minheap.add(25)
print(minheap.heap_list)
minheap.add(8)
print(minheap.heap_list)
print(minheap.retrieve_min())
print(minheap.heap_list)
print(minheap.retrieve_min())
print(minheap.heap_list)
minheap.add(1)
print(minheap.heap_list)

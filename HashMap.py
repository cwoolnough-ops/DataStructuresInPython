#implemented with seperate chaining
class HashMap():
    def __init__(self, max_size):
        self.max_size = max_size
        self.map = [None for i in range(max_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compress(self, hash_code):
        return hash_code % self.max_size

    def assign(self, key, value):
        array_room = 0
        for i in self.map:
            if i == None:
                array_room += 1
        if array_room >= 1:
            index = self.find_bucket(key)
            self.map[index] = [key, value]
        else:
            print("array_full")
        

    def find_bucket(self, key):
        array_index = self.compress(self.hash(key))
        if self.map[array_index] == None:
            return array_index
        if self.map[array_index][0] == key:
            return array_index
        count_collisions = 1
        iteration_count = 0
        while self.map[array_index][0] != key or iteration_count == self.max_size:
            new_hash_code = self.hash(key, count_collisions)
            new_index = self.compress(new_hash_code)
            if self.map[new_index] == None:
                return new_index
            if self.map[new_index][0] == key:
                return new_index
            count_collisions += 1
            iteration_count += 1
        return None

    def remove(self, key):
        index = self.find_bucket(key)
        if index != None:
            self.map[index] = None
        else:
            print("key doesnt exist")

    def retrieve(self, key):
        index = self.find_bucket(key)
        if index != None:
            return self.map[index][1]
        else:
            print("key doesnt exist")

#test cases
# map = HashMap(3)
# map.assign("2", 4)
# map.assign("3", 8)
# map.assign("4", 6)
# map.remove("4")
# map.assign("5", 7)
# print(map.map)
# print(map.retrieve("3"))gi
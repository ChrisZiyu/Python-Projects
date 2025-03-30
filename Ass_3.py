class LinearProbing:
    def __init__(self, capacity=32):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0
        self.TOMBSTONE = object()

    def __hash(self, key):
        return hash(key) % self.capacity

    def __find_slot(self, key):
        idx = self.__hash(key)
        while self.table[idx] is not None:  # Check for None first
            if self.table[idx] is not self.TOMBSTONE and self.table[idx][0] == key:  # Safely access [0]
                return idx
            idx = (idx + 1) % self.capacity
        return None

    def insert(self, key, value):
        if self.size / self.capacity > 0.7:
            self.resize()
        idx = self.__find_slot(key)
        if idx is not None:
            return False

        idx = self.__hash(key)
        while self.table[idx] is not None and self.table[idx] is not self.TOMBSTONE:
            idx = (idx + 1) % self.capacity
        self.table[idx] = (key, value)  # Assign the tuple (key, value) to table[idx]
        self.size += 1
        return True

    def resize(self):
        if self.size == self.capacity or self.size > self.capacity:

            old_table = self.table
            self.capacity *= 2
            self.table = [None] * self.capacity
            self.size = 0

            for item in old_table:
                if item is not None and item is not self.TOMBSTONE:
                    self.insert(item[0], item[1])
        return False

    def modify(self, key, value):
        idx = self.__find_slot(key)
        if idx is None:
            return False
        self.table[idx] = (key, value)
        return True

    def remove(self, key):
        index = self.__find_slot(key)
        if index is None:
            return False  # Key not found

        self.table[index] = self.TOMBSTONE
        self.size -= 1
        return True

    def search(self, key):
        index = self.__find_slot(key)
        if index is not None:  # Ensure value is not None before accessing
            return self.table[index][1]  # Safely access [1]
        return None  # Key not found

    def capacity(self):
        return self.capacity

    def __len__(self):
        return self.size

    def print_elements(self):
        for item in self.table:
            if item is not None and item is not self.TOMBSTONE:
                print(item)


hash_table = LinearProbing()  # Create a hash table

# Insert some key-value pairs
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("cherry", 30)

# Search for a key

value = hash_table.search("apple")
print(f"Value for 'apple': {value}")  # Output: Value for 'apple': 10
value = hash_table.search("banana")
print(f"Value for 'banana': {value}")  # Output: Value for 'apple': 10
value = hash_table.search("cherry")
print(f"Value for 'cherry': {value}")  # Output: Value for 'apple': 10

# Modify a value
hash_table.modify("banana", 25)
value = hash_table.search("banana")
print(f"Value for 'new banana': {value}")  # Output: Value for 'apple': 10
# Remove a key-value pair
hash_table.remove("cherry")

# Check size and capacity
print(f"Table size: {len(hash_table)}")  # Output: Table size: 2
print(f"Table capacity: {hash_table.capacity}")  # Output: Table capacity: 32 (initial capacity)

hash_table = LinearProbing(capacity=4)  # Create a smaller table (force collisions)

# Insert multiple key-value pairs to trigger resize
hash_table.insert("dog", 40)
hash_table.insert("elephant", 50)
hash_table.insert("fish", 60)
hash_table.insert("giraffe", 70)

# Check capacity after resize due to collisions
print(f"Table capacity after resize: {hash_table.capacity}")  # Output: Table capacity after resize: 8

# Search for some keys
value = hash_table.search("dog")
print(f"Value for 'dog': {value}")  # Output: Value for 'dog': 40

value = hash_table.search("elephant")
print(f"Value for 'elephant': {value}")  # Output: Value for 'elephant': 50 (might be at a different slot due to collisions)

value = hash_table.search("fish")
print(f"Value for 'elephant': {value}")

value = hash_table.search("giraffe")
print(f"Value for 'elephant': {value}")

hash_table = LinearProbing()
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("cherry", 30)
hash_table.insert("dog", 40)
hash_table.insert("elephant", 50)
hash_table.insert("fish", 60)
hash_table.insert("giraffe", 70)
hash_table.insert("eagle", 80)
hash_table.insert("tacos", 90)
hash_table.insert("f", 100)
hash_table.insert("a", 82)
hash_table.insert("as", 83)
hash_table.insert("asdasd", 84)
hash_table.insert("asr", 85)
hash_table.insert("fruit", 87)
hash_table.insert("topo", 88)
hash_table.insert("eagl", 89)
hash_table.insert("eale", 90)
hash_table.insert("agle", 180)
hash_table.insert("loto", 1280)
hash_table.insert("ea", 1180)
hash_table.insert("tripe", 11180)
hash_table.insert("ear", 11181)
hash_table.insert("taqui", 1)
hash_table.insert("comi", 123)
hash_table.insert("sprite", 100)
hash_table.insert("coke", 120)
hash_table.insert("leo", 110)
hash_table.insert("chris", 110)
hash_table.insert("juan", 110)
hash_table.insert("yun", 110)
hash_table.insert("capi", 110)
hash_table.insert("casio", 110)

print(f"Table size: {len(hash_table)}")  # Output: Table size: 33
print(f"Table capacity: {hash_table.capacity}")  # Output: Table capacity: 64 (initial capacity)
print(f"Table capacity after resize: {hash_table.capacity}")

hash_table.print_elements()

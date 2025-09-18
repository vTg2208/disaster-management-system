class HashMap:
    def __init__(self):
        self.size = 10  # Initial size of the hashmap
        self.map = [[] for _ in range(self.size)]  # List of empty lists for chaining

    def _hash(self, key):
        return hash(key) % self.size  # Simple hash function using modulo

    def add(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.map[index]):
            if k == key:  # Update the value if the key already exists
                self.map[index][i] = (key, value)
                return
        self.map[index].append((key, value))  # Add new key-value pair

    def get(self, key):
        index = self._hash(key)
        for k, v in self.map[index]:
            if k == key:
                return v  # Return value if key found
        return None  # Key not found


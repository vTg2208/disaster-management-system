class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def top(self):
        if self.heap:
            print(self.heap[0])
        else:
            print("Empty")

    def display(self):
        if self.heap:
            for item in self.heap:
                print(item)
        else:
            print("Empty")

    def _sift_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] > self.heap[parent][0]:  # Changed to '>'
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _sift_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:  # Changed to '>'
            largest = left
        if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:  # Changed to '>'
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._sift_down(largest)

    def is_empty(self):
        return len(self.heap) == 0
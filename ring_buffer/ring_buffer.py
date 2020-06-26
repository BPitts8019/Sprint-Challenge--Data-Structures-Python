class RingBuffer:
    def __init__(self, capacity):
        self.isFull = False
        self.capacity = capacity
        self.index_oldest = 0
        self.storage = []

    def append(self, item):
        if self.isFull:
            self.storage[self.index_oldest] = item
            self.index_oldest += 1
            if self.index_oldest >= self.capacity:
                self.index_oldest = 0
        else:
            self.storage.append(item)
            self.isFull = len(self.storage) == self.capacity

    def get(self):
        pass

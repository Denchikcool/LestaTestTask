from collections import deque

class FIFObyList:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость может быть представлена лишь целыми неотрицательными числами")
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def addElement(self, element):
        if self.isFull():
            raise IndexError("Буффер заполнен")
        self.buffer[self.head] = element
        self.head = (self.head + 1) % self.capacity
        self.size += 1

    def takeElement(self):
        if self.isEmpty():
            raise IndexError("Буффер пуст")
        element = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return element
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Буффер пуст")
        return self.buffer[self.tail]
    
    def clear(self):
        self.buffer = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.size = 0

#=================================================================================#

class FIFObyDeque:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Вместимость может быть представлена лишь целыми неотрицательными числами")
        self.capacity = capacity
        self.buffer = deque(maxlen = capacity)

    def isEmpty(self):
        return len(self.buffer) == 0
    
    def isFull(self):
        return len(self.buffer) == self.capacity
    
    def addElement(self, element):
        if self.isFull():
            raise IndexError("Буффер заполнен")
        self.buffer.append(element)

    def takeElement(self):
        if self.isEmpty():
            raise IndexError("Буффер пуст")
        return self.buffer.popleft()
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("Буффер пуст")
        return self.buffer[0]
    
    def clear(self):
        self.buffer.clear()
class Queue:
    def __init__(self, max_size=5):
        self.queue = [-1] * (max_size + 2)
        self.max_size = max_size
        self.start = -1
        self.end = -1
        self.currentSize = 0
    
    def enqueue(self, value):
        if self.currentSize >= self.max_size: return "Queue is full"

        if self.start == -1:
            self.start += 1

        self.end = (self.end + 1) % self.max_size
        self.queue[self.end] = value
        self.currentSize += 1

    def dequeue(self):
        if self.is_empty(): return "Queue is empty"

        if(self.currentSize == 1):
            self.start = -1
            self.end = -1
            self.currentSize = 0
            self.queue = [-1] * (self.max_size + 2)
        else:
            self.start = (self.start + 1) % self.max_size
            self.currentSize -= 1


    def is_empty(self):
        return self.currentSize == 0
    
    def is_full(self):
        return self.currentSize == self.max_size - 1
    
    def size(self):
        return self.currentSize
    def front(self):
        return self.queue[self.start]
    def peek(self):
        return self.queue[self.end]
    

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.dequeue()
queue.dequeue()
queue.enqueue(-1)
queue.dequeue()
print(queue.size())
print(queue.front())
print(queue.peek())
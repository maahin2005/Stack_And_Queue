class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, value):
        if len(self.s1):
            for _ in range(len(self.s1)-1,-1,-1):
                self.s2.append(self.s1.pop())
                
        self.s1.append(value)

        if len(self.s2):
            for _ in range(len(self.s2)-1,-1,-1):
                self.s1.append(self.s2.pop())
    
    def is_empty(self):
        return len(self.s1) == 0
    
    def dequeue(self):
        self.s1.pop()
    
    def front(self):
        print("front: " , self.s1[len(self.s1) - 1])


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.front()
queue.dequeue()
queue.front()

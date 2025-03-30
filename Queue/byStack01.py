class Queue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self,value):
        self.s1.append(value)
    
    def dequeue(self):
        if self.is_empty(): return "queue is empty!"

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()
    
    def front(self):
        if self.is_empty(): return "queue is empty!"
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        print(self.s2[-1])

    def is_empty(self):
        return len(self.s1) == 0 and len(self.s2) == 0
    

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

queue.dequeue()

queue.front()
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.end = None
        self._front = None
        self._size = 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if self._front is None:
            self._front = new_node
        if self.end is None:
            self.end = new_node
        else:
            self.end.next = new_node
        self._size += 1 
    def dequeue(self):
        popped_node = self._front.value
        self._front = self._front.next
        self._size -= 1

        print("popped_node: ", popped_node)
    def front(self):
        print("Front: ", self._front.value)

    def is_empty(self):
        print(True if self._front is None else False)

    def size(self):
        print("size of queue: ", self._size)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.front()
queue.dequeue()
queue.front()
queue.size()

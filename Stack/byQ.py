from collections import deque

class Stack:

    def __init__(self):
        self.q = deque()
        self._size = 0
    
    def push(self, value):
        self.q.append(value)
        self._size += 1

        for _ in range(self._size - 1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        if self.is_empty(): return "Stack is empty!"
        self._size -= 1
        return self.q.popleft()

    def is_empty(self):
        return self._size == 0
    
    def top(self):
        if self.is_empty(): return "Stack is empty!"

        return self.q[0]

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.pop()
stack.pop()
stack.pop()

print(stack.top())
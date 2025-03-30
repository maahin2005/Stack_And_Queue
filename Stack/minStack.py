class MinStack:
    def __init__(self):
        self._top = -1
        self.stack = []
        self._size = 0
    def push(self, value):
        if self._size == 0:
            self.stack.append((value, value))
        else:
            min_ = min(value, self.stack[self._top][1])
            self.stack.append((value, min_))

        self._size += 1
        self._top += 1
    
    def pop(self):
        if self.is_empty(): return "Stack is empty!"

        self.stack.pop()
        self._size -= 1
        self._top -= 1
    
    def top(self):
        if self.is_empty(): return "Stack is empty!"
        print(self.stack[self._top][0])
    
    def size(self):
        print(self._size)
    
    def min(self):
        if self.is_empty(): return "Stack is empty!"
        print(self.stack[self._top][1])


    def is_empty(self):
        return self._size == 0

stack = MinStack()

stack.push(20)
stack.push(10)
stack.push(30)
stack.push(40)
stack.push(2)
stack.push(50)
stack.push(5)
stack.push(6)

stack.pop()

stack.min()
stack.top()


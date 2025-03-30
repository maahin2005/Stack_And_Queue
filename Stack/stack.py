class Stack:

    def __init__(self, max_size=5):
        self.max_size = max_size
        self.stack = []
        self._top = -1

    def push(self, value):
        if self.is_full(): return "Stack is full"
        self.stack.append(value)
        self._top += 1
    
    def is_full(self):
        return self._top == self.max_size - 1
    
    def pop(self):
        if self.is_empty(): return "Stack is empty!"
        self.stack.pop()
        self._top -= 1
    
    def top(self):
        if self.is_empty(): return "Stack is empty!"

        return self.stack[self._top]
    
    def size(self):
        return self._top + 1
    
    def is_empty(self):
        return True if self._top == -1 else False
    
    def my_stack(self):
        return self.stack
    
    def peek(self):
        return self.top()
    
    def clear(self):
        self.stack = []
        self._top = -1

myStack = Stack()

print(myStack.is_empty())

myStack.push(10)
myStack.push(11)
myStack.push(12)
myStack.push(13)
myStack.push(14)
myStack.push(14)
myStack.push(14)
myStack.push(15)

print(myStack.top())
myStack.pop()
print(myStack.top())


print(myStack.my_stack())
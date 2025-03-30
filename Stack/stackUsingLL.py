class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.size = 0
        self._top = None
    def push(self, value):
       new_node = Node(value)
       new_node.next = self._top
       self._top = new_node
       self.size += 1
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        
        popped_node = self._top.value
        self._top = self._top.next
        self.size -= 1

        return popped_node

    def top(self): 
        if self.is_empty():
            return "Stack is empty" 
        return self._top.value

    def is_empty(self):
        return self.size == 0

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print(stack.top())
stack.pop()
print(stack.top())
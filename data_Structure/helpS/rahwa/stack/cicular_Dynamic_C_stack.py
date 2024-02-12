class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.size = 0
        self.top = -1

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.size == self.capacity:
            self._resize()
        self.top = (self.top + 1) % self.capacity
        self.stack[self.top] = item
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return_value = self.stack[self.top]
        self.stack[self.top] = None
        self.top = (self.top - 1 + self.capacity) % self.capacity
        self.size -= 1
        return return_value

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[self.top]

    def _resize(self):
        new_capacity = 2 * self.capacity
        new_stack = [None] * new_capacity
        for i in range(self.size):
            new_stack[i] = self.stack[(self.top - self.size + 1 + i) % self.capacity]
        self.stack = new_stack
        self.capacity = new_capacity
        self.top = self.size - 1

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(12)
stack.push(16)
stack.push(26)
stack.push(5)
print(stack.pop())  # Output: 
print(stack.peek())  # Output: 2

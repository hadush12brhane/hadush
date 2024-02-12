class Stack:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.stack = [None] * self.capacity
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.size == self.capacity:
            self._resize()
        self.stack[self.size] = item
        self.size += 1

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        self.size -= 1
        return_value = self.stack[self.size]
        self.stack[self.size] = None
        return return_value

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[self.size - 1]

    def _resize(self):
        new_capacity = 2 * self.capacity
        new_stack = [None] * new_capacity
        for i in range(self.size):
            new_stack[i] = self.stack[i]
        self.stack = new_stack
        self.capacity = new_capacity

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2

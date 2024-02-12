class CircularStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1
        self.bottom = 0

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return (self.top + 1) % self.capacity == self.bottom

    def push(self, element):
        if self.is_full():
            self.bottom = (self.bottom + 1) % self.capacity
        self.top = (self.top + 1) % self.capacity
        self.stack[self.top] = element

    def pop(self):
        if self.is_empty():
            return None
        element = self.stack[self.top]
        self.stack[self.top] = None
        self.top = (self.top - 1) % self.capacity
        return element

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]
stack = CircularStack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)  # The bottom element (1) is replaced by 6
print(stack.pop())  # Output: 6
print(stack.pop())  # Output: 5
print(stack.peek())  # Output: 4
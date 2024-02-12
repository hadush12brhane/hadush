class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def push(self, data):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        data = self.stack[self.top]
        self.top -= 1
        return data

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        return self.stack[self.top]

stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6) # Stack Overflow
print(stack.pop()) # 5
print(stack.pop()) # 4
#print(stack.peek()) # 3
print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
print(stack.pop()) # Stack Underflow

class array_Stack:
    def __init__(self, size):
        self.size = size
        self.array_Stack = [None] * size
        self.top = -1

    def push(self, data):
        if self.top == self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.array_Stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return print("the stack is know empty")
        data = self.array_Stack[self.top]
        self.top -= 1
        #print(data)
        return data
    

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        return self.array_Stack[self.top]

stack = array_Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6) # Stack Overflow
stack.push(7) 
stack.push(8) 
print("the top element before pop is:")
print(stack.peek()) # 3
print("the poped element is:")
print(stack.pop()) # 5
print("the poped element is:")
print(stack.pop()) # 4
print("the poped element is:")
print(stack.pop()) # 3print("the poped element is:")
print("the poped element is:")
print(stack.pop()) # 2
print("the poped element is:")
print(stack.pop()) # 1
print(stack.pop()) # Stack Underflow

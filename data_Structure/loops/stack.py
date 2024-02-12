"""my_Stack=list()
my_Stack.append(4)
my_Stack.append(7)
my_Stack.append(23)
print(my_Stack)
print(my_Stack.pop())
print(my_Stack.pop())
print("the left stack is")
print(my_Stack)



"""
class stack:
    def __init__(self):
        self.stack=list()
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)
my_stack=stack()
my_stack.push(45)
my_stack.push(42)
my_stack.push(78)
print(my_stack.peek())
print(my_stack)
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.peek())




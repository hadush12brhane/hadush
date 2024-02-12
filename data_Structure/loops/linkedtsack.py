"""class linkedStack:
    #def __init__(self,):
    class _Node:
        _slots__ ='_elment','_next'
        def __init__(self,element,next):
            self._elment=element
            self._next=next
        def  __ini__(self):
            self._head=None
            self._size=0
        def __len__(self):
            return self._size
        def is_empty(self):
            return self._size==0
        def push(self,e):
            self._head=self._Node(e,self._head)
            self._size+=1
        def top(self):
            if self.is_empty():
                raise Empty('stack is empty')
            return self._head._elment  
        def pop(self):
            if self.is_empty():
                raise Empty('stack is empty')
            answer=self._head._elment
            self._head=self._head._next
            self._size-=1
            return answer
    #stackl=Node(23,34)
#we=Node(23)
   # stackl.push(23)
s=linkedStack()
s._Node(123,23)"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    def pop(self):
        if self.isEmpty():
            return None
        else:
            stackTOpop= self.head
            self.head=self.head.next
            stackTOpop.next=None
            return stackTOpop.data
        #print(stackTOpop.data)
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.head.data
    def printstack(self):
        temp=self.head
        if self.isEmpty():
            print("the stack underflow")
        else:
            while temp!=None:
                print(temp.data,end="")
                temp=temp.next
                if( temp!=None):
                    print("=>",end="")
            return

if __name__=="__main__":
    myStack=stack()
    myStack.push(23)
    myStack.push(78)
    myStack.push(90)
    myStack.push(45)
    myStack.printstack()
    print("\nthe top element is ",myStack.peek())
    print("\nthe stack after poped")
    myStack.pop()
    myStack.printstack()
    print("\nthe top element is ",myStack.peek())

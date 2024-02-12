class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class singleLinkedListqueue:
    def __init__(self):
        self.rear=None
        self.front=None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return self.rear.data
        else:
            self.rear.next = new_node
            self.rear = new_node
            return self.rear.data
            

    def dequeue(self):
        if self.front is None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.data

    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end="=>")

        else:
           print("the queue is empty")
me=singleLinkedListqueue()
print(me.enqueue(12))
print(me.enqueue(3))
#me.queue(2)
#me.quueue(8)
print(me.dequeue())
me.display
"""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        else:
            temp = self.front
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return temp.data
obj=Queue()
obj.enqueue(12)
obj.enqueue(34)
print(obj.dequeue())"""
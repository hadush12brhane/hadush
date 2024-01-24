"""class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, position, data):
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for i in range(1, position - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            current.next = new_node
w=DoublyLinkedList()
print(w.insert_at_position(3,5))
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def  add(self,d):
        new=Node(d)
        if self.head==None:
            self.head=new  
        else:
            new.prev=None
            new.next=self.head
            self.head=new 
        
    def delete_first(self):
        if self.head is None:
            return "the list is empty"
        #temp = self.head
        if self.head.next is None:
            self.head = None
        else:
           # self.head = self.head.next
            self.head.next.prev = None
            self.head=self.head.next
            #self.head.prev=None
            return self.head
            #temp=None
    def deletAtEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head=None
        else:
            current = self.head
            temp=self.head
            while current.next:
                current = current.next
            current.prev.next = None
            del current

        
                
    def printList(self):
        temp=self.head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()
        
            
d=DoublyLinkedList()
d.add(4)
d.add(5)
d.add(8)
d.add(9)
d.add(8)
d.add(7)
d.add(1)
d.add(2)
d.add(3)
d.printList()
d.deletAtEnd()
d.printList()
"""d.delete_first()
d.delete_first()
d.printList()
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def pushAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            #self.head=new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_at_positione(self, position, data):
        new_node = Node(data)
        if self.head==None:
            self.head=new_node
            new_node.next=self.head
        else:
            current=self.head
            for i in range(1,position-1):
                current=current.next
            new_node.next=current.next
            current.next=new_node
            if current.next==self.head:
                new_node.next=self.head
                return "the position is out of the list range"
    
    def delete_node(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    prev.next = current.next
                    current = current.next

    def print_list(self):
        if self.head is None:
            return
        current = self.head
        while current.next != self.head:
            print(current.data, end=' ')
            current = current.next
        print(current.data)
well=CircularLinkedList()
well.pushAtEnd(34)
well.pushAtEnd(45)
well.pushAtEnd(78)
well.insert_at_positione(7,23)
well.print_list()
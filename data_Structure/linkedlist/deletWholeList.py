class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def isEmpty(self):
        if self.head==None:
            return True

    def delete_list(self):
        current = self.head
        while current:
            next_node = current.next
            del current.data
            current = next_node
        self.head = None
list1=LinkedList()
list1.push(12)
list1.push(21)
list1.push(16)
list1.push(19)
list1.push(23)
list1.delete_list()
print(list1.isEmpty())
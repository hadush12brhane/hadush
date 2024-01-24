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

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

d=LinkedList()
d.push(12)
d.push(16)
d.push(14)
d.push(23)
d.push(21)
d.push(19)
d.push(12)
d.push(1)
d.push(12)
print(d.find_middle_node())
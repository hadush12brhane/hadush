"""class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def reverse_doubly_linked_list(head):
    current = head

    # Traverse the list to reverse the pointers
    while current:
        # Swap the prev and next pointers of the current node
        current.prev, current.next = current.next, current.prev

        # Move to the next node
        current = current.prev  # Note: After swapping, the next node becomes the previous node

    # Update the head to the last node, which is now the new head
    head = current.prev

    return head
# Create a doubly linked list: 1 <-> 2 <-> 3 <-> 4
head = Node(1)
node2 = Node(2, prev=head)
node3 = Node(3, prev=node2)
node4 = Node(4, prev=node3)

head.next = node2
node2.next = node3
node3.next = node4

# Reverse the doubly linked list
head = reverse_doubly_linked_list(head)

# Print the reversed list
current = head
while current:
    print(current.data, end=" ")
    current = current.next
"""
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

    def reverse(self):
        prev = None
        current = self.head
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def printlist(self):
        current=self.head
        while current:
            print(current.data ,end=" ")
            current=current.next
        print()
p=LinkedList()
p.push(23)
p.push(12)
p.push(56)
p.printlist()
p.reverse()
p.printlist()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size

    def enqueue(self, data):
        if self.size == self.max_size:
            return False
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return True

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.size -= 1
            return temp.data

    def get_size(self):
        return self.size

    def is_full(self):
        return self.size == self.max_size

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Try to add another element to the queue
if q.enqueue(4):
    print("Element added to queue")
else:
    print("Queue is full")

# Get the size of the queue
size = q.get_size()

print(f"The size of the queue is {size}")
print(f"Is the queue full? {q.is_full()}")
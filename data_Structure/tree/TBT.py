class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.lthread = False
        self.rthread = False

def insert(root, value):
    new_node = Node(value)
    if root is None:
        root = new_node
        return root
    current = root
    while True:
        if value < current.value:
            if current.lthread:
                new_node.left = current.left
                current.left = new_node
                current.lthread = False
                new_node.right = current
                break
            else:
                current = current.left
        else:
            if current.rthread:
                new_node.right = current.right
                current.right = new_node
                current.rthread = False
                new_node.left = current
                break
            else:
                current = current.right
    return root

def delete(root, value):
    if root is None:
        return root
    current = root
    parent = None
    while current is not None:
        if value == current.value:
            break
        parent = current
        if value < current.value:
            if current.lthread:
                return root
            current = current.left
        else:
            if current.rthread:
                return root
            current = current.right
    if current.left is None and current.right is None:
        if parent is None:
            root = None
        elif current == parent.left:
            parent.lthread = True
            parent.left = current.left
        else:
            parent.rthread = True
            parent.right = current.right
    elif current.left is None or current.right is None:
        if current.left is not None:
            child = current.left
        else:
            child = current.right
        if parent is None:
            root = child
        elif current == parent.left:
            parent.left = child
        else:
            parent.right = child
        pred = get_predecessor(current)
        succ = get_successor(current)
        if current.lthread:
            pred.right = succ
        if current.rthread:
            succ.left = pred
    else:
        successor = current.right
        while not successor.lthread:
            successor = successor.left
        current.value = successor.value
        delete(root, successor.value)
    return root

def get_predecessor(node):
    if node.lthread:
        return node.left
    else:
        current = node.left
        while not current.rthread:
            current = current.right
        return current

def get_successor(node):
    if node.rthread:
        return node.right
    else:
        current = node.right
        while not current.lthread:
            current = current.left
        return current

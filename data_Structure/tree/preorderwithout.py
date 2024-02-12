class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def iterative_preorder_traversal(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        current_node = stack.pop()
        result.append(current_node.value)

        # Push right child first to ensure left child is processed first (LIFO)
        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return result

# Example usage:
# Construct a sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

preorder_result = iterative_preorder_traversal(root)
print("Preorder Traversal:", preorder_result)




"""Initialize: Start with an empty result list and a stack. Push the root node onto the stack.

While the stack is not empty:
a. Pop a node from the stack: Assign the popped node to the variable current_node.
b. Visit the current node: Append the value of the current node to the result list.

c. Push right child (if exists): If the current node has a right child, push it onto the stack.
d. Push left child (if exists): If the current node has a left child, push it onto the stack.

Continue until the stack is empty:

The stack ensures that the next node to be processed is always on top.
Return the result list: The result list contains the values of the nodes visited in preorder.

Code Explanation:

The function iterative_preorder_traversal takes the root of a binary tree as an input.

The stack is initialized with the root node. The result list is initialized to store the values of the nodes visited in preorder.

The while loop continues until the stack is empty.

Inside the loop:

The current node is popped from the stack.
The value of the current node is appended to the result list.
If the current node has a right child, it is pushed onto the stack.
If the current node has a left child, it is pushed onto the stack.
The loop continues until all nodes are visited.

The result list, containing the preorder traversal, is returned."""


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def iterative_inorder_traversal(root):
    if not root:
        return []

    result = []
    stack = []

    current_node = root

    while stack or current_node:
        # Traverse to the leftmost node
        while current_node:
            stack.append(current_node)
            current_node = current_node.left

        # Visit the current node
        current_node = stack.pop()
        result.append(current_node.value)

        # Move to the right subtree
        current_node = current_node.right

    return result

# Example usage:
# Construct a sample binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

inorder_result = iterative_inorder_traversal(root)
print("In-order Traversal:", inorder_result)

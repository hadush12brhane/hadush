class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def concatenate_linked_lists(L, M):
    # If either of the lists is empty, return the other list
    if not L:
        return M
    elif not M:
        return L
    
    # Traverse the first list (L) to find its last node
    current = L
    while current.next:
        current = current.next

    # Update the last node's next pointer to point to the first node of the second list (M)
    current.next = M

    # Return the concatenated list (LM)
    return L

# Example usage
# Creating linked list L: 1 -> 2 -> 3
L = ListNode(1, ListNode(2, ListNode(3)))

# Creating linked list M: 4 -> 5 -> 6
M = ListNode(50, ListNode(67, ListNode(69)))

# Concatenating lists L and M into LM
LM = concatenate_linked_lists(L, M)

# Printing the concatenated list LM
current = LM
while current:
    print(current.value, end="=>")
    current = current.next

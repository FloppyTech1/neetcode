class ListNode:
    def __init__(self, val):
        self.val = val # Value 
        self.prev = None # Previous pointer
        self.next = None # Next pointer

class MyLinkedList(object):
    def __init__(self):    
        self.left = ListNode(0) # Create a left dummy node
        self.right = ListNode(0) # Create a right dummy node
        self.left.next = self.right # Link them
        self.right.prev = self.left # Link them
        
    def get(self, index):
        curr = self.left.next # Skip the dummy node and enter the linked list
        while curr and index > 0: # While the list is not empty and index has not been reached
            curr = curr.next # Move to the next node
            index -= 1 # Decrease index
        if curr and curr != self.right and index == 0: # If the list is not empty and we have not reached the dummy node
            return curr.val # Return the value
        return -1 # Otherwise return -1

    def addAtHead(self, val):
        node, next, prev = ListNode(val), self.left.next, self.left # New node, the curent head and the dummy node
        prev.next = node # Assign the dummy node's next pointer to the new node
        next.prev = node # Assign the previous head's prev pointer to the new node
        node.next = next # Assign the new head's next pointer to the previous head
        node.prev = prev # Assign the new head's previous pointer to the dummy node

    def addAtTail(self, val):
        node, next, prev = ListNode(val), self.right, self.right.prev # New node, the dummy node, and the current tail
        prev.next = node # Assign the previous tail's next pointer to the new tail
        next.prev = node # Assign the dummy node's previous pointer to the new tail
        node.next = next # Assign the new tail's next pointer to the dummy node
        node.prev = prev # Assign the new tail's previous pointer to the previous tail

    def addAtIndex(self, index, val):
        curr = self.left.next # Skip the dummy node and enter the linked list
        while curr and index > 0: # While the list is not empty and index has not been reached
            curr = curr.next # Move to the next node
            index -= 1 # Decrement index
        if curr and index == 0: # If the list is not empty and we have reached the index
            node, next, prev = ListNode(val), curr, curr.prev # New node, the current node and the previous node at the index we are inserting
            prev.next = node # Assign the index - 1 node's next pointer to our new node
            next.prev = node # Assign the current index node's previous pointer to our new node
            node.next = next # Assign the new node's next pointer to the previous node at this index
            node.prev = prev # Assign the new node's previous pointer to the node that was previous to the old node at this index

    def deleteAtIndex(self, index):
        curr = self.left.next # Skip the dummy node and enter the linked list
        while curr and index > 0: # While the list is not empty and index has not been reached
            curr = curr.next # Move to the next node
            index -= 1 # Decrement index
        if curr and curr != self.right and index == 0: # If the list is not empty and we have reached the index and we aren't out of bounds
            next, prev = curr.next, curr.prev # The next node and the previous node at the index we are deleting
            prev.next = next # Assign the previous node's next pointer to the node after the index we are deleting
            next.prev = prev # Assign the node after the index we are deleting previous pointer to the node at -1 index of the node we deleted

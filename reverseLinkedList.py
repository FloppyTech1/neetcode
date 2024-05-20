class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next  # Store the next node
            curr.next = prev  # Reverse the current node
            prev = curr  # Move prev and curr pointers one step forward
            curr = nxt
        head = prev  # Update the head pointer
        return head

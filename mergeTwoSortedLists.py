class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)  # Create a dummy node to start
        curr = dummy  # Set curr to dummy node initially
        
        while list1 and list2: # While both lists are not empty
            if list1.val < list2.val: # Check for the smaller value
                curr.next = list1 # Add it to the linked list
                list1 = list1.next # Move the list to the next node
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next # Move the current pointer to the next node
        
        # If any list is left, append it to the end
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next  # Return the next of dummy which is the actual merged list

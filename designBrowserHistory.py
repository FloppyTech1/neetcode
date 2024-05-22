class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):
    def __init__(self, homepage):
        self.curr = ListNode(homepage) # Create a new node with the value as the homepage

    def visit(self, url):
        self.curr.next = ListNode(url, self.curr) # Assign the next pointer to the visited URL and assign the new node's previous pointer to the current node
        self.curr = self.curr.next # Move to the visited url

    def back(self, steps):
        while self.curr.prev and steps > 0: # Loop till we reach the url or the last node
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        
    def forward(self, steps):
        while self.curr.next and steps > 0: # Loop till we reach the url or the last node
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

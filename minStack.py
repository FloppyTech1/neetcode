class MinStack(object):

    def __init__(self):
        self.stack = [] # Initailize the main stack
        self.minStack = [] # Initialize a secondary stack to keep track of the minimum element

    def push(self, val):
        self.stack.append(val) # Push the element to the main stack
        if not self.minStack: # If the list is empty
            self.minStack.append(val) # Append the current value
        elif val <= self.minStack[-1]: # Check if the current value is less than or equal to the top element of the minStack
                self.minStack.append(val) # Append if true

    def pop(self):
        if self.minStack[-1] == self.stack[-1]: # Check if the top element of both stacks are identical
            self.minStack.pop() # Pop if true in the minimum stack
        self.stack.pop() # Pop always in the main stack

    def top(self):
        return self.stack[-1] # Return the top element

    def getMin(self):
        return self.minStack[-1] # Return the top element

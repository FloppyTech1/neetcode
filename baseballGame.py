class Solution(object):
    def calPoints(self, operations):
        myList = [] # Initialize a new list
        for i in range(0, len(operations)): # Iterate over each operation
            if operations[i] == '+': # If the operation is an addition
                prevTwo = int(myList[-1]) + int(myList[-2]) # Retrieve the last two elements in the list and add them by converting them to integers as they are currently strings
                myList.append(prevTwo) # Append the result to our list
            elif operations[i] == 'D': # If the operation is a double
                doublePrev = int(myList[-1]) * 2 # Retrieve the last element from our list, convert it to an integer, and multiply it by two
                myList.append(doublePrev) # Append the result to our list
            elif operations[i] == 'C': # If the operation is a clear
                myList.pop() # Remove the last element from the list
            else: # Otherwise, append the element as it is an integer
                newNum = int(operations[i]) # Convert it to an integer
                myList.append(newNum) # Append it

        total = sum(myList) # Calculate the total of our array
        return total # Return the result

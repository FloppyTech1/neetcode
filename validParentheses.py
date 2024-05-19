class Solution(object):
    def isValid(self, s):
        closeList = [] # Initalize a list to track which parantheses needs to be closed next
        for i in range(0, len(s)): # Loop over the string
            currBracket = s[i] # Retrieve the current parantheses in the string
            if currBracket == '(': # If it is an open parantheses
                closeList.append(')') # Append it's closing parantheses to the closing list
            elif currBracket == '{':
                closeList.append('}')
            elif currBracket == '[':
                closeList.append(']')
            elif currBracket == '}' or currBracket == ']' or currBracket == ')': # If it is a closing parantheses
                if not closeList or currBracket != closeList[-1]: # If the closing list is empty, or it is not equal to the next closing parantheses
                    return False # Return false
                else:
                    closeList.pop() # Otherwise, it is a match and we pop the closed parantheses from the closing list
        if not closeList: # Exit the loop and check if the closing list is empty
            return True # Return true
        return False # Return false

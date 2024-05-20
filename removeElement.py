class Solution(object):
    def removeElement(self, nums, val):
        leftPointer = 0 # Initialize a left pointer (slow)
        for i in range(0, len(nums)): # Loop over nums
            if nums[i] != val: # If current num is not equal to val
                nums[leftPointer] = nums[i] # Change the value at the current left pointer index
                leftPointer += 1 # Move the left pointer by one
        return leftPointer # Return the number of elements not equal to val

class Solution(object):
    def removeDuplicates(self, nums):
        leftPointer = 1 # Left (slow) pointer to keep track of where to move the next unique element
        for i in range(1, len(nums)): # Loop over the nums array
            if nums[i] != nums[i - 1]: # If the current element is different than the previous element
                nums[leftPointer] = nums[i] # Update the value at the left pointer to the current element
                leftPointer += 1 # Move the left pointer by one
        return leftPointer # Return the amount of unique elements

class Solution(object):
    def getConcatenation(self, nums):
        for i in range(0, len(nums)): # Loop over the nums array 
            nums.append(nums[i]) # Append each element to the nums array
        return nums # Return the nums array

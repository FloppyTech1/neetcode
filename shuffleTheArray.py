class Solution(object):
    def shuffle(self, nums, n):
        shuffledArray = [] # Initialize the shuffled array
        copy = n # Create a copy of n
        for i in range(0, n): # Loop n times (half the size of the array)
            shuffledArray.append(nums[i]) # First append from the first half
            shuffledArray.append(nums[copy]) # Second append from the second half
            copy += 1 # Increase the copy by 1
        
        return shuffledArray # Return result

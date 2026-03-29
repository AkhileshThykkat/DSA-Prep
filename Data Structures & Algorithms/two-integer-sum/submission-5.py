class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = dict()
        for index, num in enumerate(nums):
            complement = target - num
            if complement in compliments:
                return [compliments[complement], index]  # Return indices, not values
            compliments[num] = index  # Store num and its index
        
        return [] 
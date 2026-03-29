class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums)==0:
        #     return False
        # unique = set()
        # for i in nums:
        #     if i in unique:
        #         return True
        #     else:
        #         unique.add(i)
        # return False
        return len(set(nums))!= len(nums)
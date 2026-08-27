class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dp = set()
        for i in nums:
            if i in dp:
                return True
            dp.add(i)
        return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        re = []
        for i in nums:
            if i in re:
                return True
            else:
                re.append(i)
        return False
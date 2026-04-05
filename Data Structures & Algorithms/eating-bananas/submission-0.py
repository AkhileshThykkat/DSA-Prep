class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # so what is the speed that we can calculate 
        l = 1
        r = max(piles) # O(n)
        res = r
        while l<=r:
            k= (l+r)//2
            total_time = 0
            for p in piles:
                total_time +=math.ceil(float(p)/k)
            if total_time <=h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res
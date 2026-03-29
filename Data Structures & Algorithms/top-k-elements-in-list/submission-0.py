class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the occurances of each number among the set
        fq_counter = {}
        for n in nums:
            if n in fq_counter:
                fq_counter[n]+=1
            else:
                fq_counter[n] = 1
            
        # print(fq_counter)
        res = []
        values_list = [v for _,v in fq_counter.items()]
        values_list.sort(reverse=True)
        values_list = values_list[:k]
        for key,v in fq_counter.items():
            if v in values_list:
                res.append(key)
        return res
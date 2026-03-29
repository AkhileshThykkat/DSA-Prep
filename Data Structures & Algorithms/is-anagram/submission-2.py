class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def generate_fq_ctr(string:str)->Dict[str,int]:
            fq_ctr = {}
            for i in string:
                if i in fq_ctr:
                    fq_ctr[i]+=1
                else:
                    fq_ctr[i]=1
            return fq_ctr
        fq_ctr1 = generate_fq_ctr(s)
        fq_ctr2 = generate_fq_ctr(t)
        for key,_ in fq_ctr1.items():
            if fq_ctr1.get(key,0)!=fq_ctr2.get(key,0):
                return False
        return True
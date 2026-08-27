class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        s_ctr , t_ctr = dict(),dict()
        for i in range(len(s)):
            s_ctr[s[i]] = 1 + s_ctr.get(s[i],1)
            t_ctr[t[i]] = 1 +t_ctr.get(t[i],1)

        for key,_ in s_ctr.items():
            if s_ctr.get(key) != t_ctr.get(key,0):
                return False
        
        return True

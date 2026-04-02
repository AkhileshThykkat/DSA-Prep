class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        t = s.replace(" ","").lower()
        r = len(t)-1

        while r>l:
            while l<r and not t[l].isalnum():
                l+=1
            while r>l and not t[r].isalnum():
                r-=1
            if t[l]==t[r]:
                l+=1
                r-=1
                continue
            else:
                return False
        return True
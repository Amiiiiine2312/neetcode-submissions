class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s2) < k:
            return False
        l,r = 0,k
        while r<=len(s2):
            if sorted(s1)==sorted(s2[l:r]):
                return True
            l+=1
            r+=1
        return False
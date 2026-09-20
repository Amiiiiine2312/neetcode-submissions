class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS={}
        freqT={}
        if len(s) != len(t):
            return False
            
        for c in s :
            if c not in freqS:
                freqS[c] = 0
            freqS[c] = freqS[c]+1

        for c in t :
            if c not in freqT:
                freqT[c] = 0
            freqT[c] += 1
        
        for c in freqS:
            if c not in freqT or freqS[c] != freqT[c] : 
                return False
        return True
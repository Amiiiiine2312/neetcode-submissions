class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        maxi, m=0,0
        freq={}
        while r<len(s):
            freq[s[r]]=1+freq.get(s[r],0)
            m=max(freq.values())
            while r-l-m+1 > k :
                freq[s[l]]-=1 
                l+=1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi
            


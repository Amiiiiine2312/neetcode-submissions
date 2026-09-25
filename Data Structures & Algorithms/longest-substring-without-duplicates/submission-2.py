class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        maxlen = 0
        while r < len(s):
            while s[r] in s[l:r]:
                l+=1
            else:
                r+=1
            maxlen=max(maxlen,r-l)
        return maxlen

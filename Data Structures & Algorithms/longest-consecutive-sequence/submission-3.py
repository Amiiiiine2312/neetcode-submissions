class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set(nums)
        maxi = 0

        for i in range(len(nums)):
            if nums[i]-1 in exists:
                continue
            m = 1
            x=nums[i]
            while x+1 in exists:
                m+=1
                x+=1
            maxi = max(maxi,m)
        
        return maxi

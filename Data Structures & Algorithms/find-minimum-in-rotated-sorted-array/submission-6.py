class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0 ,len(nums)-1
        mini = nums[l]

        while l<=r : 
            m = (l+r)//2
            mini=min(mini,nums[m])
            if nums[l]<nums[m] and nums[m]>nums[r]:
                mini=min(mini,nums[l])
                l=m
            else : 
                mini=min(mini,nums[r])
                r = m-1
        return mini

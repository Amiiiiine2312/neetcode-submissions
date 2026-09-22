class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=set()
        for i in range(len(nums)):
            seenI=set()
            for j in range(i+1, len(nums)):
                tmp = -(nums[i]+nums[j])
                if tmp in seenI:
                    r=tuple(sorted([tmp,nums[i],nums[j]]))
                    res.add(r)
                else:
                    seenI.add(nums[j])
        return list(res)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        single = {}
        for i in nums:
            if i in single:
                return True
            else:
                single[i]=1
        return False
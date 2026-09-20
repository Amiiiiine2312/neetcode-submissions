class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict_values = {}
        n = len(nums)
        count_max = 0
        for i in range(n):
            dict_values[nums[i]] = nums[i]+1
        for i in nums:
            key = i
            count = 0
            while key in dict_values.keys():
                key = dict_values[key]
                count+=1
            count_max = max(count, count_max)
        return count_max 


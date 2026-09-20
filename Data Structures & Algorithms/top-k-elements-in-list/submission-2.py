class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        sortedDict = sorted(freq.items(), key=lambda x : x[1])
        for i in range(k):
            res.append(sortedDict[-i-1][0])
        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        kFreq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range (k):
            res.append(kFreq[i][0])
        return res

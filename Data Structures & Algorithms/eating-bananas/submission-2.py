class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = 0

        for i in range(len(piles)):
            maxi = max(maxi,piles[i])
        l,r = 1, maxi
        minK = maxi
        while l<r:
            m = (l+r)//2
            t = 0
            for i in range(len(piles)):
                if piles[i]%m == 0:
                    t+=piles[i]//m
                else : 
                    t+=piles[i]//m + 1
            if t <= h :
                minK=min(minK,m)
                r = m
            else : 
                l = m+1
        return minK

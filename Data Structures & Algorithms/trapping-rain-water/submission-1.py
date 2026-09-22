class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        l,r=0,len(height)-1
        maxLeft,maxRight=0,0
        while l<r:
            maxRight=max(maxRight,height[r])
            maxLeft=max(maxLeft,height[l])

            if height[l]<=height[r]: 
                water+=min(maxRight,maxLeft)-height[l]
                l+=1
            else:
                water+=min(maxRight,maxLeft)-height[r]
                r-=1
        
        return water
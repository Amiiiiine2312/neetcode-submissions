class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        start = 0
        while start < len(height) - 1:
            if height[start] == 0:
                start += 1
                continue
            end = start + 1
            while end < len(height) and height[end] < height[start]:
                end += 1
            if end < len(height):
                for i in range(start + 1, end):
                    vol += max(0, min(height[start], height[end]) - height[i])
                start = end
            else:
                maxHeight = 0
                maxPos = start + 1
                for i in range(start + 1, len(height)):
                    if height[i] >= maxHeight:
                        maxHeight = height[i]
                        maxPos = i
                for i in range(start + 1, maxPos):
                    vol += max(0, min(height[start], height[maxPos]) - height[i])
                start = maxPos
        return vol

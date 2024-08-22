class Solution(object):
    def maxArea(self, height):
        maxArea = 0
        for i, j in enumerate(height[0 : -1]):
            for m, n in list(enumerate(height))[i + 1 : ]:
                if min(j, n) * (m-i) > maxArea:
                    maxArea = min(j, n) * (m-i)
        
        return maxArea
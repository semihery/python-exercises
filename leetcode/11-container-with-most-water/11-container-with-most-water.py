class Solution(object):
    def maxArea(self, height):
        leftIndex = 0
        rightIndex = -1
        leftHeigth = height[0]
        rightHeigth = height[-1]
        maxArea = min(leftHeigth,rightHeigth)*(len(height)+rightIndex-leftIndex)


        while leftIndex + abs(rightIndex) < len(height) - 1:
            if not leftHeigth > rightHeigth:
                leftIndex += 1
                if height[leftIndex] > leftHeigth:
                    leftHeigth = height[leftIndex]
                    if min(leftHeigth,rightHeigth)*(len(height)+rightIndex-leftIndex) > maxArea:
                        maxArea = min(leftHeigth,rightHeigth)*(len(height)+rightIndex-leftIndex)

            else:
                rightIndex -= 1
                if height[rightIndex] > rightHeigth:
                    rightHeigth = height[rightIndex]
                    if min(leftHeigth,rightHeigth)*(len(height)+rightIndex-leftIndex) > maxArea:
                        maxArea = min(leftHeigth,rightHeigth)*(len(height)+rightIndex-leftIndex)

        return maxArea
class Solution(object):
    def largestAltitude(self, gain):

        alt = 0
        maxAlt = 0

        for i in gain:
            alt += i
            if alt > maxAlt:
                maxAlt = alt
        
        return maxAlt

        
        """
        :type gain: List[int]
        :rtype: int
        """
        
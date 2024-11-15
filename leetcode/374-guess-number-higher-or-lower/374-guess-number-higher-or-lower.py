# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = int(n/2)
        returnedValue = guess(x)
        if returnedValue == -1:
            step = - int((x/2) + 0.5)
        elif returnedValue == 1:
            step = int((n-x)/2 + 0.5)
        else:
            return x
        
        while True:
            x += step
            returnedValue = guess(x)
            if returnedValue == -1:
                step = - int(abs(step/2) + 0.5)
            elif returnedValue == 1:
                step = int(abs(step/2) + 0.5)
            else:
                return x
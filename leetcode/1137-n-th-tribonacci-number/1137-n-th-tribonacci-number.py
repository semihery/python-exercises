class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        lenT = 3
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        while lenT <= n:
            lenT = lenT + 1
            T.append(T[-1] + T[-2] + T[-3])

        return T[-1]
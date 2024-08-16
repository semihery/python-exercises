class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = list(t)
        j = 0
        for i in s:
            try:
                j = t.index(i, j) +1
            except:
                return False
        return True
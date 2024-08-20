class Solution(object):
    def gcdOfStrings(self, str1, str2):
        len1 = len(str1)
        len2 = len(str2)

        if len2 > len1:
            str1, str2 = str2, str1
            len1, len2 = len2, len1
        elif len1 == len2:
            return str1 if str1 == str2 else ""
        strDiff = str1[len2:]
        lenDiff = len(strDiff)
        smallerFactors = []
        def doesDivide(str1, str2, len1, len2, divisor, lenDivisor):
            if divisor * (len1/lenDivisor) == str1 and divisor * (len2/lenDivisor) == str2:
                return True
            return False

        for i in range(1, int(lenDiff ** .5) + 1):
            if lenDiff % i == 0:
                if lenDiff / i <= len2:
                    if doesDivide(str1, str2, len1, len2, strDiff[0 : lenDiff / i], lenDiff / i):
                        return strDiff[0 : lenDiff / i]

                smallerFactors.append(i)
        
        smallerFactors.reverse()
        for i in smallerFactors:
            if i <= len2:
                if doesDivide(str1, str2, len1, len2, strDiff[0 : i], i):
                    return strDiff[0 : i]

        return ""
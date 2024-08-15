class Solution:
    def reverseVowels(self, s: str) -> str:

        s = list(s)
        vowelChars = list()
        vowelIndices = list()
        for i, char in enumerate(s):
            if char in "aeiouAEIOU":
                vowelChars.append(char)
                vowelIndices.append(i)
        vowelIndices.reverse()
        for i, char in vowelIndices, vowelChars:
            s[i] = char
        return s
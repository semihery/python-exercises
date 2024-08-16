class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        result = ""
        for char in s:
            if char == " " and word:
                result = word + " " + result if result else word + result
                word = ""
            elif char != " ":
                word += char
        if word:
            result = word + " " + result if result else word + result
        return result
            
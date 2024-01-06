class Solution:
    # https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ""

        if len(str1) > len(str2):
            if not str1.startswith(str2):
                return ""
            return self.gcdOfStrings(str1[len(str2):], str2)
        
        if len(str2) > len(str1):
            if not str2.startswith(str1):
                return ""
            return self.gcdOfStrings(str2[len(str1):], str1)

        return ""
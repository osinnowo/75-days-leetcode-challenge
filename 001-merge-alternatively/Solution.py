class Solution:
    # https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i = 0
        j = 0

        while i <= len(word1) - 1 and j <= len(word2) - 1:
            char1 = word1[i]
            char2 = word2[j]
            result += (char1 + char2)
            i += 1
            j += 1
        else:
            while i <= len(word1) - 1:
                result += word1[i]
                i += 1
            
            while j <= len(word2) - 1:
                result += word2[j]
                j += 1
      
        return result
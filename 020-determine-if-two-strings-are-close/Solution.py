class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) == set(word2):
            # Check if the frequencies of characters are the same
            freq_word1 = [word1.count(char) for char in set(word1)]
            freq_word2 = [word2.count(char) for char in set(word2)]

            # Sort the frequency lists and compare
            freq_word1.sort()
            freq_word2.sort()

            return freq_word1 == freq_word2
        return False
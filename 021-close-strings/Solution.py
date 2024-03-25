from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Step 1: Check if the lengths are equal
        if len(word1) != len(word2):
            return False

        # Step 2: Count occurrences of each character
        count_word1 = Counter(word1)
        count_word2 = Counter(word2)

        # Step 3: Check if the sets of characters are the same
        if set(word1) != set(word2):
            return False

        # Step 4: Check if counts are the same
        count_values_word1 = sorted(count_word1.values())
        count_values_word2 = sorted(count_word2.values())

        return count_values_word1 == count_values_word2
    

    
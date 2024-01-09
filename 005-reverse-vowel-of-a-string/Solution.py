class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        characters = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and characters[left].lower() not in vowels:
                left += 1

            while left < right and characters[right].lower() not in vowels:
                right -= 1

            [characters[left], characters[right]] = [characters[right], characters[left]]
            left += 1
            right -= 1
        
        return "".join(characters)
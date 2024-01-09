import java.util.*;

class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
        char[] characters = s.toCharArray();

        int left = 0;
        int right = characters.length - 1;

        while(left < right) {
            while(left < right && !vowels.contains(Character.toLowerCase(characters[left]))) {
                left += 1;
            }

            while(left < right && !vowels.contains(Character.toLowerCase(characters[right]))) {
                right -= 1;
            }

            swapAt(left, right, characters);

            left += 1;
            right -= 1;
        }

        return new String(characters);
    }

    private void swapAt(int i, int j, char[] characters) {
        char temp = characters[i];
        characters[i] = characters[j];
        characters[j] = temp;
    }
}
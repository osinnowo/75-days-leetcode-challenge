class Solution {
    func reverseVowels(_ s: String) -> String {
        var vowels: Set<Character> = ["a", "e", "i", "o", "u"]
        var characters: [Character] = Array(s)
        var left = 0
        var right = characters.count - 1

        while left < right {
            while left < right, !vowels.contains { String($0) == characters[left].lowercased() } {
                left += 1
            }

            while left < right, !vowels.contains { String($0) == characters[right].lowercased() } {
                right -= 1
            }

            characters.swapAt(left, right)
            left += 1
            right -= 1
        }
        return String(characters)
    }
}
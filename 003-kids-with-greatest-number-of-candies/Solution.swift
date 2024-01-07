class Solution {
    //// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1139444110/
    func kidsWithCandies(_ candies: [Int], _ extraCandies: Int) -> [Bool] {
        var result: [Bool] = []

        guard let max = candies.max() else {
            return []
        }

        for candy in candies {
            result.append((candy + extraCandies) >= max)
        }

        return result
    }
}
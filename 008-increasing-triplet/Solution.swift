class Solution {
    func increasingTriplet(_ nums: [Int]) -> Bool {
        if nums.count < 3 {
            return false
        }

        var smallest = Int.max
        var largest = Int.max

        for num in nums {
            if num <= smallest {
                smallest = num
            } else if (num <= largest) {
                largest = num
            } else {
                return true
            }
        }

        return false
    }
}
from typing import List

class Solution:
    # // https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1139444110/
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result: list[bool] = []
        maxCandy = max(candies)
        for candy in candies:
            totalCandies = candy + extraCandies
            if totalCandies >= maxCandy:
                result.append(True)
                continue
            result.append(False)
        return result
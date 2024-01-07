import java.util.*;

class Solution {
    // https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1139444110/
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> result = new ArrayList<>();
        int max = Arrays.stream(candies).max().getAsInt();
        for(int i = 0; i < candies.length; i++) {
            int totalCandies = candies[i] + extraCandies;
            if(totalCandies >= max){
                result.add(true);
                continue;
            }
            result.add(false);
        }
        return result;
    }
}
class Solution {
    public boolean increasingTriplet(int[] nums) {
        if(nums == null || nums.length < 3) {
            return false;
        }

        int smallest = Integer.MAX_VALUE;
        int biggest = Integer.MAX_VALUE;

        for(var num: nums) {
            if(num <= smallest) {
                smallest = num;
            } else if (num <= biggest) {
                biggest = num;
            } else {
                return true;
            }
        }
        
        return false;
    }
}
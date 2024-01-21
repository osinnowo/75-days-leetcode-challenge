public class Solution {
    public int PivotIndex(int[] nums) {
        int index = 0;
        while(index < nums.Length) {    
            int leftSum = 0;
            int rightSum = 0;

            int left = index - 1;
            while(left >= 0) {
                leftSum += nums[left];
                left--;
            }

            int right = index + 1;
            while(right < nums.Length) {
                rightSum += nums[right];
                right++;
            }

            if(leftSum == rightSum) { return index; }

            index++;
        }
        return -1;
    }
}
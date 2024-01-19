class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0  # Left pointer of the window
        zero_count = 0  # Count of 0's in the current window
        max_length = 0  # Maximum length of the subarray

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # Shrink the window if there is more than one 0 in the window
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Update the maximum length
            max_length = max(max_length, right - left)

        # If max_length is equal to the length of the array, there are no 0's in the array
        return max_length if max_length < len(nums) else max_length - 1

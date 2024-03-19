class Solution {
    public int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int max = 0;

        for(var num: nums) {
            int complement = k - num;

            if(map.containsKey(complement) && map.get(complement) > 0) {
                max += 1;
                map.put(complement, map.get(complement) - 1);
            } else {
                if(!map.containsKey(num)) {
                    map.put(num, 0);
                }
                map.put(num, map.get(num) + 1);
            }
        }
        return max;
    }
}
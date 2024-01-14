class Solution {
    public boolean isSubsequence(String s, String t) {
        int index = 0;

        for(Character character: t.toCharArray()) {
            if(s.length() == index) {
                break;
            }
            if(s.charAt(index) == character) {
                index += 1;
            }
        }

        return s.length() == index;
    }
}
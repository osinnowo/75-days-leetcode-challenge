class Solution {
    //https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/
    public String gcdOfStrings(String str1, String str2) {
        if(str1.equals(str2)) {
            return str1;
        }
        if(str1.length() > str2.length()) {
            if(!str1.startsWith(str2)) {
                return "";
            }
            return gcdOfStrings(str1.substring(str2.length()), str2);
        }

        if(str2.length() > str1.length()) {
            if(!str2.startsWith(str1)) {
                return "";
            }
            return gcdOfStrings(str2.substring(str1.length()), str1);
        }
        return "";
    }
}
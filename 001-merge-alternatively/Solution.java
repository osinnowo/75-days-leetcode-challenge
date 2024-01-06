class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder sb = new StringBuilder();
        int i = 0, j = 0;
        while(i < word1.length() && j < word2.length()) {
            if(i == j) {
                sb.append(word1.charAt(i));
                i += 1;
            } else {
                sb.append(word2.charAt(j));
                j += 1;
            }
        
        while(i < word1.length()) {
            sb.append(word1.charAt(i));
            i += 1;
        }
        while(j < word2.length()){
            sb.append(word2.charAt(j));
            j += 1;
        }
        return sb.toString();
    }
}
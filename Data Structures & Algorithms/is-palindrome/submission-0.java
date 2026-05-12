class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        int n= s.length();

        for(int i=0;i<n/2;i++){
            int j=n-i-1;
            char x1=s.charAt(i);
            char x2=s.charAt(j);
            if(x1!=x2){
                return false;
            }
            
            
        }
        return true;
        
    }
}

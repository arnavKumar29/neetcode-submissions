class Solution {
    public boolean isAnagram(String s, String t) {
        int[] s1= new int[s.length()];
        int[] t1=new int[t.length()];
        for(int i=0;i<s.length();i++){
            s1[i]=(int)s.charAt(i);
        }
        for(int i=0;i<t.length();i++){
            t1[i]=(int)t.charAt(i);
        }
        Arrays.sort(s1);
        Arrays.sort(t1);
        if(Arrays.equals(s1,t1)){
            return true;
        }
        return false;
        


    }
}

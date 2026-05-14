class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        int n= nums.length;
        for(int num:nums){
            if(map.containsKey(num)){
                return true;
            }
            map.put(num,1);
        }
        return false;
        
    }
}
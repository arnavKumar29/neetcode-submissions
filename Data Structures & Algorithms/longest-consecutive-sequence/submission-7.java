class Solution {
    public int longestConsecutive(int[] nums) {
        int n= nums.length;
        
        Arrays.sort(nums);
        int lng=1;
        int curr=1;

        if(n==0){
            return 0;
        }
        for(int i=1;i<n;i++){
            if(nums[i]!=nums[i-1]){
                if(nums[i]==nums[i-1]+1){
                    curr++;

                }else{
                    lng = Math.max(lng,curr);
                    curr =1;
                }


            }
        }
        return Math.max(lng,curr);


        
    }
}

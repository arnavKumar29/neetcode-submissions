class Solution {
    public int search(int[] nums, int target) {
        int n=nums.length;
        int[] num2=new int[n];
        for(int i=0;i<n;i++){
            num2[i]=nums[i];
        }
        Arrays.sort(nums);
        for(int i=0;i<n;i++){
            if(target==num2[i]){
                return i;
            }

        }
        return -1;
        
    }
}

class Solution {
    public int findDuplicate(int[] nums) {
        int n = nums.length;

        for (int i = 0; i < n; i++) {
            int targetIndex = Math.abs(nums[i]) - 1;
            if (nums[targetIndex] < 0) {
                return Math.abs(nums[i]);
            }
            
            nums[targetIndex] *= -1;
        }
        
        return -1;
    }
}

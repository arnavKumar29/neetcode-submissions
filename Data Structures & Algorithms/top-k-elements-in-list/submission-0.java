
class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        int n = nums.length;
        int[] freq = new int[n];

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (nums[i] == nums[j]) {
                    count++;
                }
            }
            freq[i] = count;
        }

        Integer[] index = new Integer[n];
        for (int i = 0; i < n; i++) {
            index[i] = i;
        }

        Arrays.sort(index, (a, b) -> freq[b] - freq[a]);

        LinkedHashSet<Integer> set = new LinkedHashSet<>();

        for (int i = 0; i < n && set.size() < k; i++) {
            set.add(nums[index[i]]);
        }

        int[] ans = new int[set.size()];
        int i = 0;
        for (int num : set) {
            ans[i++] = num;
        }

        return ans;
    }
}
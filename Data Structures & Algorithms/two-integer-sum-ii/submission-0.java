class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;

        for (int i = 0; i < n; i++) {
            for (int j = n - 1; j > i; j--) {

                int sum = numbers[i] + numbers[j];

                if (sum == target)
                    return new int[]{i + 1, j + 1};

                if (sum < target)
                    break;
            }
        }
        return new int[]{};
    }
}
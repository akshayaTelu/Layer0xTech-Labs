public class MaxSubarraySum {
    public static int maxSubarraySum(int[] arr) {
        int maxSum = Integer.MIN_VALUE;  // Initialize maxSum to minimum integer value
        int currentSum = 0;

        for (int num : arr) {
            currentSum = Math.max(num, currentSum + num);  // Update currentSum with best option
            maxSum = Math.max(maxSum, currentSum);  // Update maxSum if currentSum is larger
        }

        return maxSum;
    }
}
package problems.hard.build_a_string;

public class BuildString {
    /**
     * Calculates the minimum cost to build the string s.
     *
     * @param a Cost to add a single character.
     * @param b Cost to copy a substring.
     * @param s The string to build.
     * @return Minimum cost to build the string.
     */
    public static int buildString(int a, int b, String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        
        // Base case
        dp[0] = 0;
        
        // For each position in the string
        for (int i = 1; i <= n; i++) {
            // Initially set cost as adding a single character
            dp[i] = dp[i - 1] + a;
            
            // Try to find any substring that can be copied
            for (int j = 0; j < i; j++) {
                int k = j;
                // Find the longest possible substring that can be copied
                while (k < i && k - j < i - k && 
                       s.charAt(k) == s.charAt(k + (k - j))) {
                    k++;
                }
                if (k > j) {  // If we found a substring that can be copied
                    dp[i] = Math.min(dp[i], dp[j] + b);
                }
            }
        }
        
        return dp[n];
    }
}


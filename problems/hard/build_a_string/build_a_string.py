def buildString(a, b, s):
    n = len(s)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        # Option 1: Add a single character
        dp[i] = dp[i-1] + a
        
        # Option 2: Try copying substrings
        for j in range(i):
            # Try all possible substrings ending at current position
            curr = s[j:i]
            pos = s[:j].rfind(curr)
            
            if pos != -1:
                # If we found a match, we can copy this substring
                dp[i] = min(dp[i], dp[j] + b)
    
    return dp[n]

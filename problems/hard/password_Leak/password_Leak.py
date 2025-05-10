def passwordLeaked(s, p):
    if not s or not p:
        return []
    
    # Create frequency maps for pattern p and initial window
    p_freq = {}
    window_freq = {}
    
    # Fill pattern frequency map
    for char in p:
        p_freq[char] = p_freq.get(char, 0) + 1
    
    # Initialize first window
    for i in range(len(p)):
        if i < len(s):
            window_freq[s[i]] = window_freq.get(s[i], 0) + 1
    
    # Initialize result list
    result = []
    
    # Check if first window is an anagram
    if window_freq == p_freq:
        result.append(0)
    
    # Slide the window
    for i in range(len(p), len(s)):
        # Remove leftmost character of previous window
        window_freq[s[i - len(p)]] -= 1
        if window_freq[s[i - len(p)]] == 0:
            del window_freq[s[i - len(p)]]
        
        # Add rightmost character of current window
        window_freq[s[i]] = window_freq.get(s[i], 0) + 1
        
        # Check if current window is an anagram
        if window_freq == p_freq:
            result.append(i - len(p) + 1)
    
    return result
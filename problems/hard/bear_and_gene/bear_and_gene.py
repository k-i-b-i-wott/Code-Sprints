def steadyGene(gene):
    """
    :param gene: string - the gene sequence
    :return: int - the length of the smallest substring to replace
    """
    n = len(gene)
    target_count = n // 4
    
    # Count frequencies of each character
    freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in gene:
        freq[char] += 1
    
    # Check if already steady
    if all(count == target_count for count in freq.values()):
        return 0
    
    # Find how many of each character we need to replace
    excess = {
        char: max(0, count - target_count)
        for char, count in freq.items()
    }
    
    # Use sliding window to find smallest substring containing excess characters
    left = right = 0
    min_length = n
    window_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    
    while right < n:
        # Expand window
        window_count[gene[right]] += 1
        
        # Try to contract window from left if possible
        while left <= right:
            can_contract = True
            for char in ['A', 'C', 'G', 'T']:
                if window_count[char] < excess[char]:
                    can_contract = False
                    break
            
            if not can_contract:
                break
            
            min_length = min(min_length, right - left + 1)
            window_count[gene[left]] -= 1
            left += 1
        
        right += 1
    
    return min_length

# Example usage
if __name__ == '__main__':
    gene = input("Enter the gene string: ").strip()
    print(steadyGene(gene))

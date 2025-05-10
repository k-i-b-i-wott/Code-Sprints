def climbingLeaderboard(ranked, player):
    # Remove duplicates from ranked scores while maintaining order
    unique_ranked = []
    for score in ranked:
        if not unique_ranked or score != unique_ranked[-1]:
            unique_ranked.append(score)
    
    # Initialize result list and pointer for ranked scores
    result = []
    i = len(unique_ranked) - 1  # Start from the lowest rank
    
    # Process each player score
    for score in player:
        # Move up the ranked list until we find a score higher than the player's
        while i >= 0 and score >= unique_ranked[i]:
            i -= 1
        
        # Add the rank (i + 2 because i is 0-based and we need to add 1 for the rank)
        result.append(i + 2)
    
    return result

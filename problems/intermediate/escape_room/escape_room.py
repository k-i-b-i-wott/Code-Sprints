def is_Disarium(num):
    # Convert number to string to iterate through digits
    num_str = str(num)
    
    # Calculate sum of each digit raised to its position (1-based)
    total = 0
    for position, digit in enumerate(num_str, 1):
        total += int(digit) ** position
    
    # Check if sum equals original number
    return total == num
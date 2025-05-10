def getPowerRange(n, a, b):
    # Find the smallest number whose nth power is >= a
    start = 1
    while start ** n < a:
        start += 1
    
    # Find the largest number whose nth power is <= b
    end = start
    while end ** n <= b:
        end += 1
    end -= 1
    
    # Return the count of numbers in the range
    return end - start + 1
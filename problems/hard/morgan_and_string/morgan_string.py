def morganAndString(a, b):
    # Add sentinel characters to handle the case when one string is exhausted
    a = a + 'z'
    b = b + 'z'
    
    # Initialize result string and indices
    result = []
    i = j = 0
    
    # Process characters until we reach both sentinels
    while i < len(a)-1 or j < len(b)-1:
        # Compare subsequences starting at current positions
        if a[i:] < b[j:]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    
    # Join characters and return result
    return ''.join(result)

# Test cases
def run_tests():
    test_cases = [
        ("ACA", "BCF", "ABCACF"),
        ("JACK", "DANIEL", "DAJACKNIEL")
    ]
    
    all_passed = True
    for i, (a, b, expected) in enumerate(test_cases, 1):
        result = morganAndString(a, b)
        passed = result == expected
        all_passed &= passed
        print(f"Test {i}:")
        print(f"Input: a = '{a}', b = '{b}'")
        print(f"Expected: '{expected}'")
        print(f"Got:      '{result}'")
        print("✓ PASSED" if passed else "✗ FAILED")
        print("-" * 40)
    
    if all_passed:
        print("\n✨ All tests passed successfully! ✨")
    else:
        print("\n❌ Some tests failed")

if __name__ == "__main__":
    run_tests()

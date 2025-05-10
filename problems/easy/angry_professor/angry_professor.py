def angryProfessor(k, a):
    """
    Determines if the class is canceled based on the number of on-time students.

    Parameters:
    k (int): The threshold number of students required for the class to not be canceled.
    a (list): A list of integers representing the arrival times of students.

    Returns:
    str: "YES" if the class is canceled, "NO" otherwise.
    """
    # Count the number of students who arrived on time or early (arrival time <= 0)
    on_time_students = sum(1 for time in a if time <= 0)
    
    # If the number of on-time students is less than the threshold, class is canceled
    return "YES" if on_time_students < k else "NO"

# Test cases
print(angryProfessor(3, [-1, -3, 4, 2]))  # ➞ "YES"
print(angryProfessor(2, [0, -1, 2, 1]))   # ➞ "NO"

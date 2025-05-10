def gradingStudents(grades):
    # Initialize an empty list to store the final grades
    final_grades = []
    
    # Iterate over each grade
    for grade in grades:
        # No rounding for grades less than 38
        if grade < 38:
            final_grades.append(grade)
        else:
            # Find the next multiple of 5
            next_multiple = (grade // 5 + 1) * 5
            # Round up if the difference is less than 3
            if next_multiple - grade < 3:
                final_grades.append(next_multiple)
            else:
                final_grades.append(grade)
    
    return final_grades

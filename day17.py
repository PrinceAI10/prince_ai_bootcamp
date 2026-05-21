def group_by_grade(students):
    result = {}
    for name, score in students.items():
        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"
        if grade not in result:
            result[grade] = []
        result[grade].append(name)
    return result



    
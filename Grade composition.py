def calculate_required_grades(prelim_grade):
    passing_grade = 75
    prelim_weight = 0.20
    midterm_weight = 0.30
    final_weight = 0.50
    grade_range = (0, 100)
    

    if not (grade_range[0] <= prelim_grade <= grade_range[1]):
        return "Preliminary grade must be between 0 and 100."
    

    current_total = prelim_grade * prelim_weight
    
 
    required_total = passing_grade - current_total
    

    midterm_final_weight = midterm_weight + final_weight
    
  
    min_required_average = required_total / midterm_final_weight
    

    if min_required_average > 100:
        return "It is not possible to achieve the passing grade with this preliminary score."
    
  
    if min_required_average < grade_range[0]:
        min_required_average = grade_range[0]
    
    return min_required_average

prelim_grade = float(input("Enter your preliminary grade: "))
result = calculate_required_grades(prelim_grade)

print(f"Minimum required average of midterm and final grades: {result:.2f}","%")
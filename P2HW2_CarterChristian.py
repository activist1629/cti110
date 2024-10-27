# Christian Carter
# October 13, 2024
# P2HW2 - List of Grades
# This program stores grades for six modules and displays key statistics about them.

# Pseudocode:
# 1. Start
# 2. Prompt the user to enter the grade for Module 1 and store it as a float.
# 3. Prompt the user to enter the grade for Module 2 and store it as a float.
# 4. Prompt the user to enter the grade for Module 3 and store it as a float.
# 5. Prompt the user to enter the grade for Module 4 and store it as a float.
# 6. Prompt the user to enter the grade for Module 5 and store it as a float.
# 7. Prompt the user to enter the grade for Module 6 and store it as a float.
# 8. Store all the grades in a list.
# 9. Calculate the lowest grade from the list using the `min()` function.
# 10. Calculate the highest grade from the list using the `max()` function.
# 11. Calculate the sum of all grades in the list using the `sum()` function.
# 12. Calculate the average of the grades by dividing the sum by the number of grades.
# 13. Display the lowest grade, highest grade, total (sum) of grades, and average.
# 14. End

grade_1 = float(input("Enter grade for Module 1: "))
grade_2 = float(input("Enter grade for Module 2: "))
grade_3 = float(input("Enter grade for Module 3: "))
grade_4 = float(input("Enter grade for Module 4: "))
grade_5 = float(input("Enter grade for Module 5: "))
grade_6 = float(input("Enter grade for Module 6: "))

grades = [grade_1, grade_2, grade_3, grade_4, grade_5, grade_6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_grades = sum(grades)
average_grade = sum_grades / len(grades)

print("\n------------Results------------")
print(f"Lowest Grade:       {lowest_grade}")
print(f"Highest Grade:      {highest_grade}")
print(f"Sum of Grades:      {sum_grades}")
print(f"Average:            {average_grade:.2f}")

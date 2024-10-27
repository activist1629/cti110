# Christian Carter
# October 20, 2024
## P3HW1
# Description: This program takes grades for six modules, calculates the lowest, highest, sum, and average,
# and determines the letter grade based on the average score.

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

print("\n----------Results----------")
print(f"Lowest Grade:     {low}")
print(f"Highest Grade:    {high}")
print(f"Sum of Grades:    {total}")
print(f"Average:          {avg:.2f}")
print("----------------------------")

if avg >= 90:
    print('Your letter grade is: A')
elif avg >= 80:
    print('Your letter grade is: B')
elif avg >= 70:
    print('Your letter grade is: C')
elif avg >= 60:
    print('Your letter grade is: D')
else:
    print('Your letter grade is: F')

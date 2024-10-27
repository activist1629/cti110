# Christian Carter
# October 27, 2024
# P3HW2 
# This program calculates an employee's weekly salary based on hours worked,
# their pay rate, and calculates additional pay for overtime hours worked.

# Pseudocode:
# 1. Prompt the user to enter the name of the employee.
# 2. Prompt the user to enter the number of hours the employee worked this week.
# 3. Prompt the user to enter the employee's pay rate.
# 4. Check if the employee worked more than 40 hours.
#    - If yes, calculate overtime hours (hours worked - 40).
#    - Calculate overtime pay (overtime hours * pay rate * 1.5).
# 5. Calculate regular hours worked (up to 40 hours).
# 6. Calculate pay for regular hours (regular hours * pay rate).
# 7. Calculate gross pay as the sum of pay for regular hours and overtime pay.
# 8. Display the employee's name, pay rate, total hours worked, overtime hours, 
#    overtime pay, regular hours pay, and gross pay.

# Begin program

employee_name = input("Enter the employee's name: ")

hours_worked = float(input("Enter the number of hours worked this week: "))

pay_rate = float(input("Enter the employee's pay rate: "))

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    regular_hours = hours_worked
    overtime_hours = 0
    overtime_pay = 0

regular_pay = regular_hours * pay_rate

gross_pay = regular_pay + overtime_pay

print("\n--- Employee Pay Summary ---")
print(f"Employee Name: {employee_name}")
print(f"Pay Rate: ${pay_rate:.2f}")
print(f"Hours Worked: {hours_worked}")
print(f"Overtime Hours: {overtime_hours}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")

# End program

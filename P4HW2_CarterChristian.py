# Christian Carter
# November 11, 2024
# P4HW2
# This program calculates the gross pay for multiple employees, 
# including overtime pay and regular pay, and displays totals for all employees entered.

# Pseudocode:
# 1. Display introductory message.
# 2. Initialize variables to track total overtime pay, total regular pay, total gross pay, and the number of employees.
# 3. Enter a loop that continues until the user enters "Done" as the employee's name.
#    a. Ask for the employee's name. Break the loop if the name is "Done".
#    b. Ask for the pay rate and hours worked.
#    c. Calculate regular pay, overtime pay, and gross pay based on hours worked:
#       - If hours worked > 40, calculate overtime pay (hours above 40 * pay rate * 1.5).
#       - Otherwise, regular pay is hours worked * pay rate.
#    d. Add the calculated overtime pay, regular pay, and gross pay to their respective totals.
#    e. Increment the employee count.
# 4. After the loop ends, display the totals: number of employees, total overtime pay, total regular pay, and total gross pay.
# 5. End the program.


print("Welcome to the Employee Payroll System!")

total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

while True:
    employee_name = input("\nEnter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == "done":
        break  
    
    try:
        pay_rate = float(input(f"Enter {employee_name}'s hours worked: "))
        hours_worked = float(input(f"Enter {employee_name}'s pay rate: "))
    except ValueError:
        print("Invalid input! Please enter numeric values for pay rate and hours worked.")
        continue

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    print(f"\nPayroll Summary for {employee_name}")
    print(f"  Hours Worked: {hours_worked}")
    print(f"  Pay Rate: ${pay_rate:.2f}")
    print(f"  Overtime Pay: ${overtime_pay:.2f}")
    print(f"  Regular Pay: ${regular_pay:.2f}")
    print(f"  Gross Pay: ${gross_pay:.2f}")

print("\nPayroll Summary for All Employees")
print("-" * 40)
print(f"Total number of employees entered: {employee_count}")
print(f"Total overtime pay: ${total_overtime_pay:.2f}")
print(f"Total regular pay: ${total_regular_pay:.2f}")
print(f"Total gross pay: ${total_gross_pay:.2f}")
print("-" * 40)

# End of program

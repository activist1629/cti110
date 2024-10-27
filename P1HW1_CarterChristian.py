# Christian Carter
# September 30, 2024
# Assignment: P1HW1
# Description: This program collects a base and an exponent from the user, calculates the power, and displays the result.
#              It also collects three integers, adds the first two, subtracts the third, and displays the result.

base = int(input("Enter the base value: 10 "))
exponent = int(input("Enter the exponent value: 5 "))

result = base ** exponent

print(f"{base} raised to the power of {exponent} is {result}!!!")

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
num3 = int(input("Enter third integer: "))


sum_result = num1 + num2
final_result = sum_result - num3


print(f"({num1} + {num2}) - {num3} = {final_result}")

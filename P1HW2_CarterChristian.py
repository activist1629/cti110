 # Christian Carter
 # September 30, 2024
 # Assignment P1HW2
 # Description: This program collects data from the user to allow them to see how much money 
 #              will be left after spending moeny on expenses for a trip.

# Pseudocode:
# 1. Start the program
# 2. Ask the user to input their budget and store it in a variable
# 3. Ask the user to input their travel destination and store it in a variable
# 4. Ask the user for the amount they will spend on gas and store it in a variable
# 5. Ask the user for the amount they will spend on accommodation and store it in a variable
# 6. Ask the user for the amount they will spend on food and store it in a variable
# 7. Add the gas, accommodation, and food expenses together to calculate total expenses
# 8. Subtract the total expenses from the budget to find the remaining budget
# 9. Print the travel destination
# 10. Print the total expenses with a message
# 11. Print the remaining budget with a message
# 12. End the program

budget = float(input("Enter your budget: $"))  
destination = input("Enter your travel destination: ") 
gas_expense = float(input("Enter how much you will spend on gas: $")) 
accommodation_expense = float(input("Enter how much you will spend on accommodation: $")) 
food_expense = float(input("Enter how much you will spend on food: $"))

total_expenses = gas_expense + accommodation_expense + food_expense

remaining_budget = budget - total_expenses 


print("\nTravel Destination:", destination)
print("Total Expenses: $", format(total_expenses, ".2f"))
print("Remaining Budget: $", format(remaining_budget, ".2f")) 

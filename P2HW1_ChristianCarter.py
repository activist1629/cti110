# Christian Carter
# October 13, 2024
# P2HW1 - Travel Expense
# This program calculates and formats travel expenses.

destination = input("Enter your travel destination: ")

budget = float(input("Enter your budget for the trip: $"))
gas = float(input("How much do you think you will spend on gas? $"))
hotel = float(input("Approximately, how much will you need for accommodation? $"))
food = float(input("How much do you plan to spend on food? $"))

total_expenses = gas + hotel + food

balance = budget - total_expenses

print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${hotel:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print(f"{'Total Expenses:':<20}${total_expenses:,.2f}")
print(f"{'Remaining Balance:':<20}${balance:,.2f}")

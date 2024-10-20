# Christian Carter
# October 20, 2024
# P3LAB 
# Description: This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies
# needed to make the given amount of money. The user inputs a float value representing money in dollars.

def calculate_coins(amount):
    total_cents = int(amount * 100)

    dollars = total_cents // 100
    total_cents %= 100
    
    quarters = total_cents // 25
    total_cents %= 25

    dimes = total_cents // 10
    total_cents %= 10

    nickels = total_cents // 5
    total_cents %= 5

    pennies = total_cents // 1

    if dollars > 0:
        print(f"{dollars} dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} penn{'y' if pennies == 1 else 'ies'}")

def main():
    user_input = input("Enter an amount of money (e.g., 12.34): ")
    try:
        amount = float(user_input)
        if amount < 0:
            print("Please enter a non-negative amount.")
            return
        calculate_coins(amount)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()

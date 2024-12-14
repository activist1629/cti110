# Christian Carter
# November 17, 2024
# P5LAB
# Brief description: This program simulates a self-checkout machine, calculating change owed 
# and breaking it into denominations (dollars, quarters, dimes, nickels, pennies).

import random

def disperse_change(change):
    """
    This function calculates and displays the number of dollars, quarters, dimes,
    nickels, and pennies required for the given change amount.
    :param change: The amount of change owed to the customer.
    """
    # Convert change to cents to avoid floating-point errors
    cents = round(change * 100)
    
    # Calculate denominations
    dollars = cents // 100
    cents %= 100
    
    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10
    
    nickels = cents // 5
    cents %= 5
    
    pennies = cents
    
    # Display the result
    print("\nChange owed:")
    print(f"Dollars  : {dollars}")
    print(f"Quarters : {quarters}")
    print(f"Dimes    : {dimes}")
    print(f"Nickels  : {nickels}")
    print(f"Pennies  : {pennies}")

def main():
    """
    Main function to run the self-checkout simulation.
    """
    # Generate a random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")
    
    # Prompt user for payment
    while True:
        try:
            payment = float(input("Enter amount paid: "))
            if payment < total_owed:
                print("Insufficient payment. Please enter an amount greater than or equal to the total owed.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Calculate change
    change_owed = round(payment - total_owed, 2)
    print(f"\nPayment: ${payment:.2f}")
    print(f"Change: ${change_owed:.2f}")
    
    # Call disperse_change function
    disperse_change(change_owed)

# Call the main function
if __name__ == "__main__":
    main()

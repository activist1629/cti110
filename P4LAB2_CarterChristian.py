# Christian Carter
# November 3, 2024
# P4LAB2

def display_multiplication_table(number):
    """Displays multiplication table for a given number from 1 to 12."""
    for i in range(1, 13):  
        print(f"{number} x {i} = {number * i}")

def main():
    while True:  
        try:
            user_input = int(input("Enter an integer: "))
            
            if user_input >= 0:
                print(f"\nMultiplication table for {user_input}:")
                display_multiplication_table(user_input)
            else:
                print("Error: Cannot accept negative values.")
            
            repeat = input("Do you want to run the program again? (yes/no): ").strip().lower()
            
            if repeat == "no":
                print("Exiting the program. Goodbye!")
                break
            elif repeat != "yes":
                print("Invalid input. Exiting the program.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

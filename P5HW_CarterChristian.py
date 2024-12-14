# Christian Carter
# November 24, 2024
# P5HW 
# This program is a menu-driven math quiz game. It generates random numbers and asks the user to either add or subtract them. The user can guess the answer, and the program provides feedback. The program terminates only if the user enters "3".

import random

def display_menu():
    """Displays the menu options to the user."""
    print("\nMath Quiz")
    print("1. Addition Quiz")
    print("2. Subtraction Quiz")
    print("3. Exit")

def addition_quiz():
    """Generates two random numbers, adds them, and asks the user to guess the sum."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 + num2

    print(f"\nWhat is {num1} + {num2}?")
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Congratulations! That's correct.")
    else:
        print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")

def subtraction_quiz():
    """Generates two random numbers, subtracts them, and asks the user to guess the difference."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = num1 - num2

    print(f"\nWhat is {num1} - {num2}?")
    user_answer = int(input("Your answer: "))

    if user_answer == correct_answer:
        print("Congratulations! That's correct.")
    else:
        print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")

def main():
    """Main function to control the program flow."""
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            addition_quiz()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Call the main function to start the program.
if __name__ == "__main__":
    main()

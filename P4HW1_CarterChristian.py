# Christian Carter
# November
# P4HW1
# A brief description: This program collects user-defined number of scores, validates them, calculates 
# the average after dropping the lowest score, and determines the corresponding letter grade.

# Pseudocode:
# 1. Display introductory message.
# 2. Ask the user how many scores they would like to enter and store this number.
# 3. Create an empty list to store valid scores.
# 4. Use a loop to repeatedly ask the user to enter scores until the desired number of valid scores is collected.
#    a. For each input, check if the score is valid (between 0 and 100).
#    b. If invalid, prompt the user to re-enter the score until a valid score is entered.
#    c. Add valid scores to the list.
# 5. After collecting all scores:
#    a. Identify and display the lowest score.
#    b. Remove the lowest score from the list and display the modified list.
#    c. Calculate and display the average of the scores in the modified list.
#    d. Determine and display the letter grade corresponding to the average.
# 6. End the program.

def determine_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

print("Welcome to the Score Processing Program!")
num_scores = int(input("Enter the number of scores you would like to enter: "))

scores = []

for i in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{i + 1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("Invalid score! Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

lowest_score = min(scores)
scores.remove(lowest_score)
average_score = sum(scores) / len(scores)
grade = determine_grade(average_score)

print("\nResults")
print("-" * 20)
print(f"Lowest score dropped: {lowest_score}")
print(f"Modified list of scores: {scores}")
print(f"Scores average: {average_score:.2f}")
print(f"Letter grade: {grade}")
print("-" * 20)

# End of program

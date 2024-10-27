# Christian Carter
# October 6, 2024
# Assignment: P2LAB2_CarterChristian
# Description: This program creates a dictionary of cars with their MPG values, allows the user to select a car, input miles to drive, and calculates the gallons of gas needed.

vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

keys = vehicle_mpg.keys()

print("Available vehicles:")
for vehicle in keys:
    print(vehicle)

selected_vehicle = input("\nEnter the name of the vehicle you want to drive: ")

if selected_vehicle in vehicle_mpg:
    
    mpg = vehicle_mpg[selected_vehicle]
    
    miles = float(input(f"Enter the number of miles you will drive the {selected_vehicle}: "))
    
    gallons_needed = miles / mpg
    
    print(f"\nThe {selected_vehicle} gets {mpg} miles per gallon.")
    print(f"You will need {gallons_needed:.2f} gallons of gas to drive {miles} miles.")
else:
    print("The vehicle you entered is not in the list. Please make sure you enter the name exactly as shown.")

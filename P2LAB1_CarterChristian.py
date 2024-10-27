# Christian Carter
# October 6, 2025
# Assignment: P2LAB1_CarterChristian
# Description: This program calculates the diameter, circumference, and area of a circle given its radius.

radius = float(input("Enter the radius of the circle: "))

diameter = 2 * radius

circumference = 2 * 3.14159 * radius  

area = 3.14159 * (radius ** 2)

print(f"\nDiameter: {diameter:.1f}")  
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")

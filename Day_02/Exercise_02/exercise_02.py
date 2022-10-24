# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight/(height * height)
print(f"Your BMI is:{round(BMI)}")

# Instructions:
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

Age = int(input("How old are you?"))
max_age = 90
num_days_left = (max_age - Age) * 365
num_weeks_left = (max_age - Age) * 52
num_month_left = (max_age - Age) * 12

Message = (f"You have {num_days_left} days, {num_weeks_left} weeks, and {num_month_left} months left.")

print(Message)

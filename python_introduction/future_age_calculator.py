#!/usr/bin/env python3
# future_age_calculator.py
# Calculate user's age in the year 2050 based on their current age

# Prompt the user to input their current age
current_age = int(input("How old are you? "))

# Years difference between 2023 and 2050
years_to_add = 2050 - 2023

# Calculate future age
future_age = current_age + years_to_add

# Print the result
print(f"In 2050, you will be {future_age} years old.")

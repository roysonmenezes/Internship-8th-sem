# Assignment Name : Smart Input Program
# Description : Build a Python program that takes name, age, hobby and prints a personalized message while categorizing age using conditionals.

# Smart Input Program

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorize age using conditionals
if age < 13:
    category = "a child"
elif age < 20:
    category = "a teenager"
elif age < 60:
    category = "an adult"
else:
    category = "a senior citizen"

# Print personalized message
print("\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are {age} years old, which means you are {category}.")
print(f"It's great to know that your hobby is {hobby}. Keep enjoying it!")

# Assignment (20/02/2026)

# Assignment Name : Student Data Manager
# Description : Store data for 5 students using dictionaries, print topper, class average, and assign grades.

# Student Data Manager

# Dictionary storing student names and marks
students = {
    "Rahul": 85,
    "Sneha": 92,
    "Arjun": 76,
    "Priya": 88,
    "Kiran": 69
}

# Calculate class average
total_marks = sum(students.values())
average = total_marks / len(students)

# Find topper
topper = max(students, key=students.get)

# Function to assign grade
def assign_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "D"

# Print student details with grades
print("---- Student Report ----")
for name, mark in students.items():
    grade = assign_grade(mark)
    print(f"{name} : {mark} - Grade {grade}")

print("\nClass Average:", round(average, 2))
print("Topper:", topper, "-", students[topper])
# Day 1 Python Practice - Bhuvana G - PSNACET
# Topic: Variables and Data Types

# Your personal info stored as variables
name = "Bhuvana"
college = "PSNACET"
branch = "Information Technology"
year = 3
cgpa = 8.5
is_aiml_student = True

# Print all information
print("===== My Profile =====")
print("Name:", name)
print("College:", college)
print("Branch:", branch)
print("Year:", year)
print("CGPA:", cgpa)
print("AIML Student:", is_aiml_student)

# Data type check
print("\n===== Data Types =====")
print(type(name))      # string
print(type(year))      # integer
print(type(cgpa))      # float
print(type(is_aiml_student))  # boolean

# Simple calculation
total_semesters = year * 2
print("\nCompleted semesters:", total_semesters)
print("Remaining semesters:", 8 - total_semesters)
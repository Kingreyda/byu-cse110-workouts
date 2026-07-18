# Ask the user for the grade
grade = float(input("\nPlease input your grade: "))

# Figure out the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Get the last digit
last_digit = grade % 10

# Determine the sign
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else: sign = ""

# Handle exceptions
if (letter == "A" and sign == "+") or letter == "F":
    sign = ""

# Display the letter grade
if grade >= 70:
    print(f"\nYour grade is {letter}{sign}")
    print("Congratulations you have passed this course.")
else:
    print(f"\nYour grade is {letter}{sign}")
    print("Please try again, you have failed.")
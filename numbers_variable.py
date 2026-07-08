import math

# Number Variables
age = int(input("\nHow old are you? "))
print(f"On your next birthday, you will be {age + 1}")

eggs_carton = int(input("\nHow many egg cartons do you have? "))
eggs_result =  eggs_carton * 12
print(f"You have {eggs_result} eggs.")

cookies = float(input("\nHow many cookies do you have? "))
people = int(input("How many people are there? "))
cookies_result = cookies / people
print(f"Each person may have {cookies_result} cookies.")

#Standard Format Style
number = 323.2202
print("\nYour number is ${:.2f}".format(number))

#Scientific Notation
print()
distance = (23 + 32) // 4
print(f"The distance is {distance:.2e} meters.")

#Grouping Numbers
big_number = 2828827781
print(f"\nThe big number is: {big_number:,}.")
print(f"The big number is: {big_number:_}.")

#Libraries
height = 1.54
higher = math.ceil(height)
lower = math.floor(height)

print(f"\nOverall Higher: {higher} Overall Lower: {lower}")

###Number section###
first_number = int(input("\nWhat is the first number? "))
second_number = int(input("What is the second number? "))


if first_number > second_number:
    print("The first number is greater")
else:
    print("The first number is not greater")

if first_number == second_number:
    print("The numbers are equal")
else:
    print("The numbers are not equal")

if second_number > first_number:
    print("The second number is greater")
else:
    print("The second number is not greater")

###Animal section###
animal = input("\nWhat is your favourite animal? ").lower()

if animal == "dog":
    print("That's my favourite animal too")
else:
    print("That one is not my favourite")

###Temperature section###
temprature = float(input("\nWhat is the temprature outside? "))

if temprature < -15:
    print("It's too cold. Don't go!")

elif temprature < 5:
    weather = input("What is the weather like (cold, rainy, snowy)? ").lower()

    if weather in ["cold", "rainy", "snowy"]:
        print("Maybe you should stay home.")
    else:
        print("You should go but be vigilant")

else: 
    print("Enjoy your run.")

###Age section### 
try:
    age = int(input("\nWhat is your age? "))
    
    if age >= 18:
        print("YAY! You're an adult")
    else:
        print("You're still a minor")
except:
    print("Please enter a number")

rewards = 0
choice = "cookie"
total_order = 9

if (choice == "cookie" or choice == "drink") and total_order > 3:
    rewards =+ 5
print(f"You have {rewards} rewards")
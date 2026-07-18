"""
Author: Olaribigbe King David
Purpose: Adventure Game Assignment
Title: BELLY WALLY: TWO SIDES OF CAMPUS
"""
# Creative Addition: 
# This adventure game contains a hidden questionnaire.
# The player's choices reveal food ordering preferences,delivery expectations,
# and spending habits while still presenting the experience as an interactive story.

# I also created the game with two hidden story paths. 
# Depending on the player's choices, they may continue the adventure as 
# a hungry student or unexpectedly become a Belly Wally student delivery runner. 

print("\n===================================")
print(" BELLY WALLY: TWO SIDES OF CAMPUS ")
print("===================================")

print("\nYou wake up late and your first class started 15 minutes ago.")
print("Your stomach growls and your phone is buzzing on the table..")

choice1 = input("\nDo you CHECK your phone or IGNORE it? ").lower()


if next == "next":
    print("\nYou wake up late for class.")
    print("Your phone is buzzing beside your bed.")
    print("You are hungry, tired, and already running behind schedule.")

    choice1 = input("\nDo you CHECK your phone, GO to class, or SLEEP? ").lower()
    if choice1 == "check":
        print("")


else:
    print("\nGame Over!")
    next = input("\nType NEXT to start over (1 life remains): ")

    if next == "next":
        print("\nYou wake up late for class.")
        print("Your phone is buzzing beside your bed.")
        print("You are hungry, tired, and already running behind schedule.")
    else:
        print("Game Over!")
        exit()
   
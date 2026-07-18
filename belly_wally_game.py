"""
Author: Olaribigbe King David
Purpose: Adventure Game Assignment
Title: BELLY WALLY: TWO SIDES OF CAMPUS
"""
# Creative Addition: 
# This adventure game has two hidden story paths, depending on the player's choices.
# The player may continue as a hungry student or unexpectedly become a Belly Wally student delivery runner.

# This game also contains a hidden questionnaire.
# The player's choices reveal food ordering preferences, delivery expectations,
# and spending habits while still presenting the experience as an interactive story.

# I also added ratings and titles to reward players. 

print("\n===================================")
print(" BELLY WALLY: TWO SIDES OF CAMPUS ")
print("===================================")

# Welcome display
print("WELCOME PLAYER!")
print("Hint: choices are displayed in ALL CAPS")
print("Titles are assigned at the final stage")
print("\nSelect your choice and shape your world.")

# BELLY WALLY GAME STARTS
start_game = input("\nPress NEXT to continue: " ).lower()

if start_game == "next":
    print("\nYou wake up late and your first class started 15 minutes ago.")
    print("Your stomach growls and your phone is buzzing on the table.")

    choice1 = input("\nDo you CHECK your phone, GO to class, or SLEEP? ").lower()

# Question option one

    if choice1 == "check":
        print("\nYou unlock your phone and a notification appears:")
        print("Your scheduled Belly Wally delivery has been waiting for pickup for 20 minutes!.")
        print("You freeze...")
        print("Then you remember!")
        print("You signed up as a Belly Wally student runner last week to earn extra cash.")

        choice2 = input("\nDo you RUN, CALL or IGNORE? ").lower() 

        if choice2 == "run":
            print("\nYou grab your backpack and sprint out the door.")
            print("The customer is waiting for breakfast before class.")

            choice3 = input("\nDo you take the SHORTCUT or MAINROAD? ").lower()

            if choice3 == "shortcut":
                print("\nCongratulations!")
                print("You arrive in record time.")
                print("The customer gives you a 5-star rating and a tip.")
                print("Title: CAMPUS DELIVERY HERO")
                print("Your Belly Wally Rating: ⭐⭐⭐⭐⭐")

            elif choice3 == "mainroad":
                print("\nCongratulations!")
                print("Although you lose a star point, you arrive a little late but safely.")
                print("The customer appreciates your professionalism.")
                print("Title: RELIABLE RUNNER")
                print("Your Belly Wally Rating: ⭐⭐⭐⭐")
            else:
                print("\nOUCH!")
                print("Game Over!")

        elif choice2 == "call":
            print("\nYou quickly place the call and the client picks up...!")

            choice3 = input("\nDo you APOLOGIZE or EXPLAIN? ").lower()

            if choice3 == "apologize":
                print("\nCongratulations!")
                print("The customer appreciates your honesty.")
                print("You keep your 5-star rating.")
                print("Title: THE TRUSTED RUNNER")
                print("Your Belly Wally Rating: ⭐⭐⭐⭐⭐")


            elif choice3 == "explain":
                print("\nCongratulations!")
                print("The customer understands.")
                print("You are given another chance to complete the delivery.")
                print("Title: THE LUCKY ONE")
            else:
                print("\nThe customer hangs up in confusion.")
                print("Game Over!")

        elif choice2 == "ignore":
            print("\nYou ignore the notification and go back to bed.")
            print("When you wake up, the order has been cancelled.")
            print("Your Belly Wally rating drops and you get fired.")
            print("Game Over!")

        else:
            print("\nThat is not one of the choices.")
            print("Game Over!")
            
# Question option two

    elif choice1 == "go":
        print("\nYou rush to class.")
        print("Halfway there, your stomach growls loudly.")

        choice2 = input("\nDo you BUY food, or WAIT? ").lower()

        if choice2 == "buy":
            choice3 = input("\nDo you prefer CHEAP, FAST, or HEALTHY food? ").lower()
            
            if choice3 == "cheap":
                print("\nCongratulations!")
                print("You always look for the best deals.")
                print("Title: THE BUDGET MASTER")
                

            elif choice3 == "fast":
                print("\nCongratulations!")
                print("You value convenience and quick delivery.")
                print("Title: THE SPEED SEEKER")

            elif choice3 == "healthy":
                print("\nCongratulations!")               
                print("You prefer nutritious meals.")
                print("Title: THE HEALTH CHAMPION")

            else:
                print("\nThat choice doesn't exist.")
                print("Game Over!")
        
        elif choice2 == "wait":

            choice3 = input("\nDo you WAIT until LUNCH or DINNER? ").lower()

            if choice3 == "lunch":
                print("\nCongratulations!")
                print("You barely survive the hunger till lunch.")
                print("Title: THE IRON BELLY")

            elif choice3 == "dinner":
                print("\nYou spend the whole day hungry and pass out before dinner.")
                print("Game Over!")

            else:
                print("\nThat wasn't a valid option.")
                print("Game Over!")
        else:
            print("\nThat wasn't a valid option.")
            print("Game Over!")

# Question option three

    elif choice1 == "sleep":
        print("\nYou decide to ignore reality and go back to sleep.")
        print("Three hours later, you wake up and class is over.")

        choice2 = input("\nDo you APOLOGIZE or PRETEND nothing happened? ").lower()
        
        if choice2 == "apologize":
            choice3 = input("\nDo you EMAIL or rather CALL your instructor? ").lower()

            if choice3 == "email":
                print("\nCongratulations!")
                print("Your instructor appreciates the honesty.")
                print("Title: THE RESPONSIBLE SLEEPER")

            elif choice3 == "call":
                 print("\nCongratulations!")
                 print("You explain the situation and get another chance.")
                 print("Title: THE LUCKY STUDENT")
            else:
                print("\nNo one knows what you're trying to do.")
                print("Game Over!")
        
        elif choice2 == "pretend":
            choice3 = input("\nDo you BLAME TRAFFIC or BLAME WIFI? ").lower()
 
            if choice3 == "traffic":
                print("\nYou lie and nobody believes you.")
                print("Game Over!")
 
            elif choice3 == "wifi":
                print("\nYou lie and nobody believes you.")
                print("Game Over!")

            else:
                print("\nYour excuse makes no sense.")
                print("Game Over!")
    else:
        print("\nYour world ended")
        print("Game Over!")

else:
    print("\nYour world ended at the beginning")
    print("Game Over!")
    exit()

print("\nThanks for playing BELLY WALLY: TWO SIDES OF CAMPUS!")
exit("\n")

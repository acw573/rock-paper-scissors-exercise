
# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock','paper','scissors': ")

#print(user_choice)
print("USER CHOICE: ",user_choice)


# validate the input such that only if it is one of the expected values will we continue
# ...with the rest of the program otherwise we'll stop the program before it tries to do anything else
#...and we'll ask the user to run the program again

#double equal sign is for equality checking

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, INVALID INPUT. PLEASE TRY AGAIN.")
    exit()


valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOICE: ",computer_choice)

if user_choice == "rock":
    if computer_choice == "rock":
        print("IT'S A TIE")
    elif computer_choice == "paper":
        print("MAYBE NEXT TIME. THE COMPUTER WON!")
    elif computer_choice == "scissors":
        print("YOU WON! AMAZING!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("YOU WON! AMAZING!")
    elif computer_choice == "paper":
        print("IT'S A TIE")
    elif computer_choice == "scissors":
        print("MAYBE NEXT TIME. THE COMPUTER WON!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("MAYBE NEXT TIME. THE COMPUTER WON!")
    elif computer_choice == "paper":
        print("YOU WON! AMAZING!")
    elif computer_choice == "scissors":
        print("IT'S A TIE")


print("THIS IS THE END OF OUR GAME. PLEASE PLAY AGAIN.")
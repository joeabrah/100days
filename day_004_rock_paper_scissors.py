import random

#Define the variables for each action using ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Definitions: Rock = 0, Paper = 1, Scissors = 2

#Print welcome statement
print("Welcome to the Rock, Paper, Scissors game!")

#Takes user input for which type, by word and converts it to lower case
user_selection = input("Do you choose Rock, Paper, or Scissors? Please type out the word:\n")
lower_selection = user_selection.lower()

#Converts the selection to an integer
if lower_selection == "rock":
    selection = 0
elif lower_selection == "paper":
    selection = 1
elif lower_selection == "scissors":
    selection = 2
else:
    selection = 3

#Creates a random integer for the program's random action, and ensure it's converted to words for printing
rand_int = random.randint(0, 2)
if rand_int == 0:
    comp_selection = "Rock"
    print(rock)
elif rand_int == 1:
    comp_selection = "Paper"
    print(paper)
elif rand_int == 2:
    comp_selection = "Scissors"
    print(scissors)

#If then statements to determin the winner
if selection == rand_int:
    print(f"You chose {user_selection}, the computer chose {comp_selection}, it's a DRAW!")
elif selection == 0:
    if rand_int == 1:
        print(f"You chose {user_selection}, the computer chose {comp_selection}, you LOSE!")
    elif rand_int == 2:
        print(f"You chose {user_selection}, the computer chose {comp_selection}, you're the winner!")
elif selection == 1:
    if rand_int == 0:
        print(f"You chose {user_selection}, the computer chose {comp_selection}, you're the winner!")
    elif rand_int == 2:
        print(f"You chose {user_selection}, the computer chose {comp_selection}, you LOSE!")
elif selection == 2:
    if rand_int == 0:
        print(f"You chose {user_selection}, the computer chose {comp_selection}, you LOSE!")
    elif rand_int == 1:
        print(f"You chose {user_selection}, the computer chose {comp_selection}, you're the winner!")
else:
    print("You chose an invalid option, you lose!")

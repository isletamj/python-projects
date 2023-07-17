import random

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

choices = [rock, paper, scissors]
computerChoice = random.randint(0, 2)

userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if userChoice < 0 or userChoice > 2:
    print("Invalid Number: valid numbers are from 0 to 2 ONLY")
    exit()

print("You chose: \n" + choices[userChoice])

print("The computer chose: \n " + choices[computerChoice])

if userChoice == computerChoice:
    print("It's a draw")
elif (userChoice == 0 and computerChoice == 1) or (userChoice == 1 and computerChoice == 2) or (
        userChoice == 2 and computerChoice == 0):
    print("You lose")
elif (userChoice == 0 and computerChoice == 2) or (userChoice == 1 and computerChoice == 0) or (
        userChoice == 2 and computerChoice == 1):
    print("You win!")

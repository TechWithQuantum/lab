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

choices = ["Rock", "Paper", "Scissors"]
random_choices = random.choice(choices)

# print(random_choices)

choice = int(input("Which do you choose? Type 1 for rock, 2 for paper, or 3 for scissors: "))

if choice == 1 and random_choices == "Rock":
    print(f"You chose Rock {rock}\nComputer chose {random_choices} {rock} \nResult is: TIE")

elif choice == 1 and random_choices == "Paper":
    print(f"You chose Rock {rock}\nComputer chose {random_choices} {paper} \nResult is: WIN")

elif choice == 1 and random_choices == "Scissors":
    print(f"You chose Rock {rock}\nComputer chose {random_choices}{scissors} \nResult is: LOSE")

elif choice == 2 and random_choices == "Rock":
    print(f"You chose Paper {paper}\nComputer chose {random_choices} {rock} \nResult is: WIN")

elif choice == 2 and random_choices == "Paper":
    print(f"You chose Paper {paper}\nComputer chose {random_choices} {paper} \nResult is: TIE")

elif choice == 2 and random_choices == "Scissors":
    print(f"You chose Paper {paper}\nComputer chose {random_choices}{scissors} \nResult is: LOSE")

elif choice == 3 and random_choices == "Rock":
    print(f"You chose Scissors {scissors}\nComputer chose {random_choices}{rock} \nResult is: LOSE")

elif choice == 3 and random_choices == "Paper":
    print(f"You chose Scissors {scissors}\nComputer chose {random_choices}{paper} \nResult is: WIN")

elif choice == 3 and random_choices == "Scissors":
    print(f"You chose Scissors {scissors}\nComputer chose {random_choices}{scissors} \nResult is: TIE")
else:
    print("Invalid Choice. Please read instructions, and try again.")



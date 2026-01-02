print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_question = input("You have two doors to choose from. Enter door 'right' or 'left'\n")

if first_question == "left":
    second_question = input("Choose if you want to 'swim' or 'wait'\n")
    if second_question == "wait":
        third_question = input("Which door do you want to enter through? red, blue, or yellow?\n")
        if third_question == "red":
            print("You've been burned by fire. GAME OVER")
        elif third_question == "blue":
            print("You've been eaten by beasts. GAME OVER")
        elif third_question == "yellow":
            print("You've found the treasure! YOU WIN.")
        else:
            print("Game Overrrrrr")
    else:
        print("You were attacked by trout. GAME OVER")
else:
    print("You've fallen into a hole! GAME OVER")
    exit()

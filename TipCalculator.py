print("Welcome to the Tip Calculator 3000!")
bill = float(input("What is the bill total?\n"))
tip = int(input("What percentage do you want to add as a tip?\n"))
people = int(input("How many people are splitting the bill?\n"))
print("Calculating...\n")
total_bill = (bill + (bill * (tip / 100)))
pay_per_person = (total_bill / people)

print(f"Your bill total, including the tip is: {total_bill}, and you've chosen to split the payment among {people} people, which gives the amount each person would pay: {pay_per_person}.\n")

print("Thank you for using Tip Calculator 3000!")


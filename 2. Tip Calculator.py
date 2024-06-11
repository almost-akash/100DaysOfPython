print("Welcome to the Tip Calculator")
total = float(input("What was the Total Bill?\n"))
num_of_people = int(input("How many people to Split it up with\n"))
percentage_tip = int(input("What Percentage Tip would you like to give?\n"))
per_person = (total + (total * percentage_tip / 100)) / num_of_people
print("Each person should pay " + str(round(per_person,1)))
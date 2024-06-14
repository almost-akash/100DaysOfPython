import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")
noOfLetters = int(input("How many letters would you like in your password\n"))
noOfNumbers = int(input("How many numbers would you like in your password\n"))
noOfSymbols = int(input("How many symbols would you like in your password\n"))

if noOfSymbols.is_integer() or noOfLetters.is_integer() or noOfNumbers.is_integer():
    password = []

    for char in range(1, noOfLetters+1):
        password += random.choice(letters)
    for char in range(1, noOfNumbers+1):
        password += random.choice(numbers)
    for char in range(1, noOfSymbols+1):
        password += random.choice(symbols)
else:
    print("Invalid value, enter a number instead.")

random.shuffle(password)

if len(password) <= 6:
    print("Your password is weak, try to include at least 8 characters for a stronger password.")
elif len(password) == 7:
    print("Your password is medium, try to include at least 8 characters for a stronger password.")
else:
    print(f"Your password is {''.join(password)}.")
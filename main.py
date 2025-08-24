import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n--> "))
nr_numbers = int(input(f"How many numbers would you like?\n--> "))
nr_symbols = int(input(f"How many symbols would you like?\n--> "))

letters_picked = []
numbers_picked = []
symbols_picked = []

for number in range(0, nr_letters):
    random_index = random.randint(0,len(letters))
    letter_pick = letters[random_index]
    letters_picked.append(letter_pick)

for number in range(0, nr_numbers):
    random_index = random.randint(0,len(numbers))
    number_pick = numbers[random_index]
    numbers_picked.append(number_pick)

for number in range(0, nr_symbols):
    random_index = random.randint(0,len(symbols))
    symbol_pick = symbols[random_index]
    symbols_picked.append(symbol_pick)

password = letters_picked + numbers_picked + symbols_picked
random.shuffle(password)
print(f'Your randomized password is:\n--> {"".join(password)}')


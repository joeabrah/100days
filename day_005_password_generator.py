#Password Generator Project
import random

#Creates the initial lists (Given in class) for the characters available
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Prints the welcome message
print("Welcome to the PyPassword Generator!")

#Asks for inputs for how many letters, numbers, and symbols the user wants
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Creates the blank list to fill the characters into
password = []

#Each of these defines the for loop to place the random choice characters into the password list only for the number of characters desired
for char in range(1, nr_letters + 1):
    letter_char = random.choice(letters)
    password += letter_char

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

#Shuffles the password list
random.shuffle(password)

#Creates the random_password string variable for the randomized password
random_password = ""

#Adds in each character in the password list into the random_password string
for char in password:
    random_password += char

#Prints the random password
print(random_password)

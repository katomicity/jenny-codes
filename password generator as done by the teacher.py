import random
import string
letters = string.ascii_letters
numbers = string. digits
character = string. punctuation
password = []

L = int(input("How many letters would you like in your password \n :-"))
N = int(input("How many numbers would you like in your password\n:-"))
C = int(input("How many Symbols would you like in your password \n:-"))

for i in range (1, L +1):
    print (i)
    char = random.choice(letters)
    password += char
for i in range(1, N +1):
    char =random.choice(numbers)
    password += char
for i in range(1, C +1):
    char = random.choice(character)
    password += char
    
random.shuffle(password)
password = "".join(password)
print(password)
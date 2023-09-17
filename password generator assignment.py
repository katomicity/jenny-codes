import string
import random
 
print ("Welcome to my password generator")
#how ever in her tutorial she just listed down the lerrers numbers and symbols
#but in python you can import them using the string function as below.
letters = string.ascii_letters
numbers = string. digits
character = string. punctuation


L = int(input("How many letters would you like in your password \n :-"))
N = int(input("How many numbers would you like in your password\n:-"))
C = int(input("How many Symbols would you like in your password \n:-"))


x = random.sample(letters, L)
y = random.sample(numbers, N)
z = random.sample(character, C)

'''
print(letters)
print(numbers)
print(character)
print(x)
print(y)
print(z)
'''
#after a
password = x+y+z
random.shuffle(password)
#the join function uses "" or '' but you can play around by incuding ':'.join(words) where : will be the new separator
#words = ['apple', 'banana', 'cherry']
#result = ':'.join(words)
#print(result) output ==>  apple:banana:cherry


password = "".join(password)

print(f"Your random password is {password}")
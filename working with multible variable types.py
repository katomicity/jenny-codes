
print(len("emmanuelkato"))
print(len("12345"))
name = input("What is your name? ")
length=len(name)
print(name)
print("your name, " + name + " has " + str(length) + " characters")
#To concatenate + variables of different types we convert the old man out to the variable type which the others posess like in the above example
#len which gives integers was converted to string to give the meaning full output below
"""
int()
float()
str()
bool()
"""
print("10"+"10")
print(int("10")+int("10"))
print(10+float("10"))
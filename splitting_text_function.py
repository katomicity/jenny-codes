"""
list.split(separator):
The above function separates items in a given list according to a separator creteria
"""
name = "my name is emmanuel kayiwa kato"
print (name)
name_split = name.split(" ")
print(name_split)

#Assignment
#Who will clean the Utensils Today.
import random
washer= input("Input Names of your Family Members Separated by a Comma :-")
list = washer.split(",")
print(random.choice(list) + " will be the one to Wash Utensils Today")


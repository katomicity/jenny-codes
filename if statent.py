#CONDITIONAL STATEMENTS IN PYTHORN
"""
In pythorn decisions are deciced upon by conditional statements like if ,else and else if "elif"
the program below returns the brand of majarine to buy according to the price i buy
"""
blueband=input("Whats the price of blueband majarine at shorprite?")
prestige=input("whats the price of prestige majarine at best buy?")

if prestige >= blueband:
    print("Buy blueband")
else:
    print("Buy prestige")
#if follows indetion ie if and else have to be on the same indetion line while also the print statements have to be on the same indetion
height= input("Please Enter Your Height in Feet")
if(int(height)>3):
    print("Buy Token")
    print ("Now You can board the Metro")
else:
    print("No Token Required")
#incase the else or elif is left hanging with northing the part satisfying the condition of else or el if is not printed
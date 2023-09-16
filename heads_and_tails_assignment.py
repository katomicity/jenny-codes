import random
list=[0,1]
a = random.choice(list)
ans=input("Write in  H or h for heads and T or t for tails ")
if (ans == "H" or ans == "h") and a == 0 :
     print("You Win Heads is the Correct Answer")
elif (ans == "H" or ans == "h") and a == 1 :
     print("You Lose Tails is the correct Answer")
elif (ans == "T" or ans == "t") and a == 1 :
     print("You Win Tails is the Correct Answer")
elif (ans == "T" or ans == "t") and a == 0 :
     print("You Lose Heads is the correct Answer")
else:
     print("Check if you wrote t,T,H,h if else please contact the Operator")
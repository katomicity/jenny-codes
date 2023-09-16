import random
set = [1,2,3]
answer = random.choice(set)

guess = int(input("WHATS YOUR CHOICE?\n 1:- Rock \n 2;- Paper \n 3:- scissors \n    --" ))
print(guess)
#1
if guess == answer:
    print("Draw")
elif guess != answer:
    if guess == 1 and answer == 2:
        print("You loose Paper WINS")
    elif guess == 1 and answer == 3:
        print("Yow WIN Scissors Lost")
    elif guess == 2 and answer == 1 :
        print("You WIN Rock lost")
    elif guess == 2 and answer == 3 :
        print("You loose Scissors WIN")
    elif guess == 3 and answer == 1:
        print("You loose Rock WINS")
    elif guess == 3 and answer == 2:
        print("You WIN Paper lost")
    else:
        print("Input the Choices Using the given numbers only")
else:
    print("Error Contact Game Techinician @kemmasoft")

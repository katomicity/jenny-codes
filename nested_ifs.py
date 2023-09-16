#elif function is only for the more than three conditions ie: 
#unlike else and if which completes two conditions elif does more than that
height = int(input("What is Your Height in Feet? -"))
if height>3:
    print("can ride")
    age = int(input("What is your age? -"))
    if age <=9 :
        print("Pay 500 Ugshs")
    elif age <16 :
        print("Pay 1000 Ugshs")
    else:
        print("Riding Is only for children but You are advised to pay for a Friend or Relative")
else:
    print("Cannot Ride , Your height is out of range.   Sorry For Being Short.")
"""
if statements are tricky because for the above case we hace two cases.
1):-
the height can be okay but when the age is not so to write following conditions you have to write the if for the first condition
and on the next indent you write another if again.
2):-
we use elif in the second condition to cater for the third opinion. ie elif covers the second or more conditions on that level
so that else can cover its last condition
Note:-
"if " are the levels of the decision making in flowchat ie you first do the conditions that level like in a game to move to another level
which still can be in a general level code of the game stage.
howeer all if's have to be closed by an else.
"""
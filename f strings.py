name="Emmanuel"
age=25
height=1.6

# print("My name is" + name + ". Iam " + age+ "years o1d." + "My height is " + height +"meters"  )
# There two ways to correct the line above

#By using commas to term as string:
print("My name is" ,name, "Iam " ,age, "years o1d. My height is " ,height, "metres" )
#when using commas i leave out the plus sign

#By using f string  ie adding  {} to the variables
print(f"My name is {name} Iam  {age},  years o1d.  My height is {height}  metres. ")
#The advantage with f string is that you write the "" once and  then you dont reapeat them
#Also the calculations can be used in f strings
print(f"In 2030 i will be {age + 7} years old.")
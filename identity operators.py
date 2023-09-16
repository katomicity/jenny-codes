#IDENTITY OPERATORS
a=5
b=5
print(a is b)
"""
in the above true is returned from a comparison in the memory adress ie. when a = 5 'a' is just linked
with the memory adress of 5 so on stating that b = 5 b is  also just then linked with the above same adress of 5.
So the checker for the is function checks whether the memory adresses are the same but it dosent
check the values as the checker for the comparison operators of (a==b)
"""
print(id (a))
print(id (b))

a = '5'
#If a is altered to a string then the result and adresses are changed as shown below
print(a is b)
print(id(a))
print(id(b))
#Therefore, the expression
print(id(a)==id(b))
#Is the same as
print(a is b)
#IS NOR FUNCTION
print(a is not b)
b='5'
print(id(a) is not id(b))
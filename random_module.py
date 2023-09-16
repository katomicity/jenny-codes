import random
"""
random.random():
Returns a random float number between 0 and 1 ony (inclusive of 0, but not 1).
"""
a = random.random()
print(a)

"""
random.uniform(a, b): 
Returns a random float number between a and b (inclusive of a and b).
"""
a1 = random.uniform(1, 2)
print(a1)
"""
random.randint(a, b): 
Returns a random integer between a and b (inclusive of both a and b).
"""
b = random.randint(1,4)
print(b)

"""
random.randrange(start, stop[, step]): Returns a random element from the range(start, stop, step).
It is similar to range(), but it returns a randomly selected element from the specified range.
The function below retuns randomly 1,3,7 since there the values at the second step.
"""
c = random.randrange(1,8,2)
print(c)

"""
random.choice(seq)
This function returns a random item from a list,
tuple, or string.
"""
d=[2,5,7,90,-4,20,-12,23,-5]
e=random.choice(d)
print(e)
"""
random.shuffle(lst)
This function is used to randomize the items of a
list in place. It returns Nothing.
"""
random.shuffle(d)
print(d)
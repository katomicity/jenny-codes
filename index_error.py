#NEGATIVE INDEXING IN PYTHON 
set = [ 20,30,40,90]
print(set[0])
print(set[-4])
print(set[int(len(set)/-1)])
"""
The above code details that len as a negative gives us the 20 but
when its positive it will give us index error this is because the
negative index is counted from backwards while the positive is counted from
the front with zero inclusive hence negative indexing starts from negative -1
"""

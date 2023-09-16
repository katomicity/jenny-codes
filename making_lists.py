#lists can store numbers, integers,booleans and floats in either mixed types or single types values 
#included but each value must be separated bu a comma(,) as shown below
roll_no = [1,2,3,4,5]
print(roll_no)
names  = ["jenny" ,"ram" ,"shyam"]
print(names)
mix_list = ['jenny' , True , 10.10]
print(mix_list)
#A certain number from a set can be printed alone by writing down its indes position but you must put in 
#mind that indexes start from 0 to 1 to 2 and so on
numbers = [-1,0,1,2,3,4,5,6,]
print(numbers[0])
print(numbers[2])
"""
From the example above the the items of that index position are printed but now for a range.
A range follows an order of the index to length to step ie :
the index is the starting position to a certain length like below
"""
print(numbers[7])
print(len(numbers))
print(numbers[1:7])
"""
the above instruction prints the values from the index position of 1 which is 0 to the length of 7 which is 5
for the next part is the step simply meaning skip by a position,this simply jumps over the values intructed by it as below
"""
print(numbers[1:7:2])
"""
the instruction above skips over from the starting point 0 then one position of 1 then prints the number in the second position
which is two jumps/skips 3 one position then delares 4 wich is second position and ends since the range is over
"""
#OTHER FUNCTIONS
number = [-4,0,7,2,4,3,5,-2,-1]
number.sort()
print(number)
#the sort function aranges in the ascending order smmallest to bigest
number.reverse()
print(number)
print(max(number))
print(min(number))
#the reverse just re writes the items from the last to the first
#NB:- the sort and reverse functions cannot be used together with the print function its only first executed then you can print it
# sorting reversing max and min dont work on mixed type lists

#ADDING ITEMS TO THE LIST 
#the added  number goes at the end of the list
number.append(1)
print(number)

#ADDING items at a position in a list 
#the insert funtion follows the index position to item creteria as below
number.insert(2,-17)
print(number)

#ADDING MANY ITEMS ON THE LIST
number.extend([-19,-20,-18])
print(number)

#CHANGING ITEMS IN A SET OR LIST just mention the index
number[2]=13

#for a range of 5,-17,4 we follow the order of index to length to state that range and for this is 1:4
number[1:4]=[21,22,23]
print(number)

#REMOVING AN ITEM just mention the exact item
number.remove(23)
print(number)
#however if there two similar items the first one with a near or small index position
#REMOVING USING POP(INDEX)
#like above pop also removes but when given the index position
print(number.pop())
print(number)
#without any parameter of index pop just removes the last value


#OTHER FUNCTIONS 
#list.clear() deletes or removes all items in the list
#list.count(x)  how many times x value appears in the list
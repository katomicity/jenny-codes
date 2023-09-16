#BITWISE OPERATORS
#AND & FUNCTION
a=5
b=4
print(a&b)
"""
a =5 =101 in binary
b =4 =100 in binary 
0101--->a
0100--->b
0100--->answer for a&b which is 4 in base ten or in decimal
Therefore, "&" Results bit 1,if both operand bits are 1;otherwise results bit 0.
"""

#OR | FUNCTION
print(a|b)
"""
0101--->a
0100--->b
0101--->answer for a|b which is 5 in base ten
Therefore, "|" Results bit 1,if any of the operand bit is 1; otherwise results bit 0.
"""
#XOR ^ FUNCTION
print(a^b)
"""
0101--->a
0100--->b
0001--->answer for a^b which is 1 in base ten
Therefore, "^" Results bit 1,if one of the operand bit is 1 ie.(1 and 0) but not both ie.(1  1,0  0), otherwise results bit 0.
"""
#LEFT SHIFT << FUNCTION
print(a<<2)
"""
The left operand’s value is moved toward left by the number of bits
Its like rounding to decimal places but in bits
a = 0101 a<<2 = 010100 ---> 20
ie.0101.000000 "carry two bit places to the left side where they appear" 010100.0000
we add bits here
"""
#RIGHT SHIFT >> FUNCTION
print(b>>2)
"""
The left operand’s value is moved toward right by the number of bits 
Its like rounding off decimal places but in bits
b = 0100 b>>2 = 0001 --->1
ie for a byte 8 bits 00000100. "carry two bit places to the right side where they disappear" 000001.
we lose bits here
"""
#NOT ~ FUNCTION
print(~a)
"""
~a =~5 =~0101
Note: all bits are written in either nibble ,byte ,kilobyte and above
~a means -(a + 1 bit)
In bit addition
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 0 cary 1 to the next bit
Soln;
0101
+  1
0110
-(0110)---->-6 therefore ~a = -6
poofing the above answer
a means +(~a - 1 bit)
In bit subtraction
1 - 1 = 0
1 - 0 = 1
0 - 1 = 1(with a Borrow of 1 from the next high order digit)
Note: "The borrowed 1 bit from the high order digit has a value of 2 not 1"
0110
-  1
0101
hence a =5 =0101 in binary

"""
#NEGATIVE BITS IN PYTHON
print(~a)
print(~b)
"""
The result -5 or -6 can be expressed in bit form by either Signed magnitude form or The 2's complement method
SIGNED MAGNITUDE FORM
Here the first bit from the left is inversed ie.
-6---> -(0110)---> signed 1110
The first bit of the nible has been inversed to a 1 as '1' represents postive and '0' represents negatve, "this method is not usually used because it limits addition and
subtraction of bits since the meaning of the bit 6 has been altered to 14 in the example above.
Whats left after the signed is what is called the magnitude.
2's COMPLEMENT METHOD
This is the most accurate way negatve bits can be expressed ,even unlike in the first method the bits in 2's complement can be read by
the computer.
In this method, the whole digit is invesed in the term First Complement
~a =-6 = -(0110) ---> 1001
~b =-5 = -(0101) ---> 1010
Then:
2nd Complement where 1 is added to the result of the 1st Complement

~a =-6 ---> 1001 + 1 --->1010
~b =-5 ---> 1010 + 1 --->1011
proof since a nibble 4 bit:
powers of 2 up to 2**4
8  4  2  1
for a -8 + 2 = -6
for b -8 + 2 + 1 = -5

The first number to attain a power ie."the first one"  is given a -ve
"""
#ADDITION AND SUBTRACTION OF NEGATIVE BITS
print(~a+b)
print(~a-b)
"""
Because of the accuracy of the 2's complement, There used in addition and subtraction of negatives
~a+b
 1010 --->~a
+0100 ---> b
 1110 ---> -2
 converting -2 back to a positve means x= (y - 1) where y is the inversed x ie.
 y = 0001
 0001
 +  1
 0010 ---> 2
 however, for an operation like below:
 p = 43 = 101011 --6bit
 q = -71 = -(1000111) --7bit
 by 2's complement -71 = 0111001 --6bit
  00111001
 +00101011
  01100100
however, in bit addition and subtraction the number if is a carried at the end is not valid. 6bit and a six bit give us a six bit the rest is null and void
 00101011 -->43
-01000111 -->- 71
 00100100
 
 In the same example above, the scenario of 0-1 happens which therefore we write zero and the rest after is null and void.
"""


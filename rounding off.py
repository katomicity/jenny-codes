#ROUNDING OFF IN PYTHON
#round(number, No of digits)
#if no number of digits is not indicated the system predicts a zero and the
#output is not a float but an integer. For a float you have to write the zero
print(round(7.61))
print(round(7.61,0))
print(round(7.61,1))
#There special cases when the number is to be rounded is becoming odd
print(round(6.5))
#since 6.5 becomes 7 which is not even the nearest even 6 is picked
print(round(674,-1))

#Negative numbers round off to the nearest power of 10
print(round(674,-1))
print(round(674,-2))
print(round(665,-1))
"""
e;
 round(674,-1)--->670 is the closest to 10^1
 round(674,-2)--->700 is the closest to 10^2
 however by time breaking rule the odd numbers affect
 round(665,-1)--->660 is closest even number to 10^1
 time breaking only occurs when there is only one whole integer and there no other place values on the same side of the decimal point
 however placevalues also matter in time breaks
 """
print(round(6.5))
print(round(7.5))
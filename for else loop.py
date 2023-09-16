#for else loop is uniqe because the second else condition is only met if the
#loop is conpleted first
tuple1 =(2,56,34,3,4,-1)
for i in tuple1 :
    if  i ==5:
        print(i)
        break
else :
    print ("error")



for i in tuple1 :
    if  i ==4:
        print(i)
        break
else :
    print ("error")

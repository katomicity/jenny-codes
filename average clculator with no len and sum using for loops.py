list = (input("state the numbers for average separated by a comma :"))
list = list.split(',')
newlist = []
for i in list:
    y = int(i)
    #print(y)
    newlist.append(y)

print(newlist)
result = []
x=0
count=0

for i in newlist:
    count = count +1
    x = i + x
    #print(x)
    result.append(x)

#print(result)
    
i#ndex=(count-1)
#total = result[index]
#print(count)
total = max(result)
average= total / count
average = round(average,)

print(f"The average of {count} items with a total of {total} is {average}" )
#to get maximum number
m = newlist[0]
for i in newlist:
    if  i > m:
        m = i

print(i)
#151,153,140,160,167

row1 = ["\U0001F644", "\U0001F644", "\U0001F644"]
row2 = ["\U0001F644", "\U0001F644", "\U0001F644"]
row3 = ["\U0001F644", "\U0001F644", "\U0001F644"]

set = [row1,row2,row3]

position = input("Where is the money?")
#32
row = int(position[0])
column = int(position[1])
#remember the rows are always less by a -1 to the length so we just have to subtract
#then we can now choose the right row set by index which was selected
true_row = set[row -1]
#Since we have arrived at that set now we need to go to the value selected by the user and modify it
true_row[column-1]= "X"
print(f"{row1}\n{row2}\n{row3}") 
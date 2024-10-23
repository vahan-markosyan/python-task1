list = [1,2,2,3,4,5,3,5,6]
newList = []
for i in list:
    if i not in newList:
        newList.append(i)
print(newList)        
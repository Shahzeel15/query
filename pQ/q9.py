# second largest no in list 
def secondleg(list1):
    maxlist=max(list1)
    list2=[]
    for i in range(0,len(list1)):
        if list1[i] != maxlist:
            list2.append(list[i])
    return max(list2)

list=[1,2,4225,664,3]
print(secondleg(list))
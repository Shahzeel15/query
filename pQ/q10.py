# remove dublicates from a list 
def dub(list1):
    unique=[]
    for i in range(0,len(list1)):
        if list1[i] not in unique:
            unique.append(list1[i])
    return unique
list=[1,1,2,22,2,2,2,3,3,3,4,4,7,8]
print(dub(list))
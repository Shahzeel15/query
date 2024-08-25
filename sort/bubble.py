# bubblesort 
def sort(list1):
    for i in range(0,len(list1)-1):
        for j in range(0,len(list1)-1):
            if(list1[j+1]<list1[j]):
                temp=list1[j+1]
                list1[j+1]=list1[j]
                list1[j]=temp
    return list1
list1=[5,4,3,2,1,6,7,8,9,34,34,2,23,12]
print(sort(list1))
            
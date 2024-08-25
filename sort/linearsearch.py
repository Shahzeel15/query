#linear search
def searchl(l1,s):
    for i in range(0,len(l1)):
        if(l1[i]==s):
            print("found at index : ",i+1)
            break
    
l1=[1,2,3,3,4,5,6,6,7,3]
print(searchl(l1,3))
# Write a Python function that takes two lists and returns True if they have at least one
# common member.

def comp (lis1,lis2):
    for i in range(0,len(lis1)):
        for j in range(0,len(lis2)):
            if(lis1[i]==lis2[j]):
                print("meat equal ... ",lis1[i],lis2[j])
                return True

list1=[10,20,30,40,50]
list2=[23,34,49,45,40]
print(comp(list1,list2))

def bool(boolt):
    if(boolt==True):
        print("hey")

bool(comp(list1,list2))
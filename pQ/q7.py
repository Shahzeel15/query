# common element btw two list 
def common(l1,l2):
    common_ele=[]
    for i in range(0,len(l1)):
        for j in range(0,len(l2)):
            if(l1[i]==l2[j]):
                if l1[i] not in common_ele:
                    common_ele.append(l1[i])
    return common_ele

l1=[1,2,3,4,5,6]
l2=[2,3,4,4,7,8]
print(common(l1,l2))

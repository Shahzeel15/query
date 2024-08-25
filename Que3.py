# max no in list 
def larget(no_list):
    max=no_list[0]
    for i in range(0,len(no_list)):
        if(no_list[i]>max):
            max=no_list[i]
    return max
print(larget([1,222,23,384,5]))
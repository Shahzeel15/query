#sum and avg of elements in list 
def sum(no_list):
    sum=0
    for i in range(0,len(no_list)):
        sum=sum+no_list[i]
    avg=sum/len(no_list)
    return sum,avg
print(sum([1,2,3,4,5]))

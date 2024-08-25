# count the freq of each element in the list 
def freq(list):
    freqnum={}
    for i in range(0,len(list)):
        if list[i] in freqnum:
            freqnum[list[i]]+=1
        else:
            freqnum[list[i]]=1
    return freqnum

lista=[1,1,1,2,2,1,3,2,4,3,5]
print(freq(lista))
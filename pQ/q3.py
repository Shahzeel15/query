# largest element in list 
def large(lista):
    return max(lista)

lista=[566,78,99,25,637]
print(large(lista))

def l2(lista):
    max=lista[0]
    for i in range(0,len(lista)):
        if(lista[i]>max):
            max=lista[i]
    return max
print(l2(lista))
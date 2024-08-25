# fact of a number 
def fact( n ):
    factt=1
    for i in range(1,n+1):
        factt=factt*i
    return factt
n=int(input())
print(fact(n))

# recursion 
def factrec(n):
    if(n==0):
        return 1 
    else:
        return n*factrec(n-1)
    
print(factrec(n))
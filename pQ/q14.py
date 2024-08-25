# fibonacci series
n=int(input())
print(0,1,end=" ")
n1=0
n2=1
n3=0
for i in range(1,n):
    n3=n1+n2
    print(n3,end=" ")
    n1=n2
    n2=n3
    
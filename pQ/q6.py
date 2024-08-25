# prime no or not 
def prime(n):
    if (n==1 or n==0):
        print("it's not prime no")
    else:
        count=0
        for i in range(2,n):
            if(n%i==0):
                print("it's not prime no")
                count+=1
        if(count==0):
            return True
        else:
            return False
        
n=int(input())
print(prime(n))

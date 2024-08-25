#fact
# no=int(input())
# ans=1
# for i in range(1,no+1):
#     ans=ans*i
# print(ans)

#recursion
def fact(no):
    if no==0 :
        return 1
    else:
        return no*fact(no-1)
    
no=int(input())
print(fact(no))
   
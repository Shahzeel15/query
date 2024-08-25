# palindrome no 
no=int(input())
temp=no
reverse=0
while temp>0:
    reminder=temp%10
    reverse=(reverse*10)+reminder
    temp=temp//10
print(reverse)
if(no==reverse):
    print("yes")
else:
    print("no")
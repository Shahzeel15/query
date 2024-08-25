#armstrong no 

no = int(input())
temp=no
arm=0
square=1
count=0
while (temp>0):
    reminder=temp%10
    count+=1
    temp=temp//10
print(count)
temp=no
while(temp>0):
    reminder=temp%10
    square=reminder**count
    arm=arm+square
    temp=temp//10
print(arm)
if(arm==no):
    print("yes")
else:
    print("no")

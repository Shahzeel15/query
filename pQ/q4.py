# reverse str 
str=input("enter str : ")
print(str[::-1])
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")

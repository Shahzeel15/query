#Program to find area of a circle using function use single return value function with argument
def area(radius):
    ans=3.14*radius*radius
    return ans 

radius=int(input("enter radius : "))
print("Area is ",area(radius))